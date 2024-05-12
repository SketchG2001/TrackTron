from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.utils.timezone import datetime
from django.contrib import messages
from employee.models import Attendance
from django.http import HttpResponse
from django.template.loader import render_to_string
import csv


@login_required
def reports(request):
    emp_id = request.user.id
    username = request.user.username

    # Get current month and year
    current_month = datetime.now().month
    current_year = datetime.now().year

    # Filter attendance records for the current month
    attendance_records = Attendance.objects.filter(
        employee_id=emp_id,
        date__year=current_year,
        date__month=current_month
    )

    # Count attendance statuses for the current month
    attendance_counts = attendance_records.values('status').annotate(count=Count('status'))

    # Initialize counts for present, absent, and late
    present_count = 0
    absent_count = 0
    late_count = 0

    # Update counts based on the aggregated values
    for count in attendance_counts:
        if count['status'] == 'present':
            present_count = count['count']
        elif count['status'] == 'absent':
            absent_count = count['count']
        elif count['status'] == 'late':
            late_count = count['count']

    return render(request, 'employee/reports.html', {
        'username': username,
        'emp_id': emp_id,
        'attendance_records': attendance_records,
        'present_count': present_count,
        'absent_count': absent_count,
        'late_count': late_count
    })


@login_required
def all_employees(request):
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to access this page.')
        return redirect('dashboard')

    if request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        requested_month = request.GET.get('month')
        requested_year = request.GET.get('year')

        if requested_month and requested_year:
            try:
                requested_month = int(requested_month)
                requested_year = int(requested_year)

                # Filter Attendance records for the requested month and year
                reports = Attendance.objects.filter(
                    date__year=requested_year,
                    date__month=requested_month
                )

                if reports.exists():
                    # Render the reports template with the loaded reports
                    html_response = render_to_string('hradmin/reports_partial.html', {'reports': reports})
                    return HttpResponse(html_response)
                else:
                    return HttpResponse('No data available for this month.')
            except ValueError:
                return HttpResponse('Invalid month or year.')
        else:
            return HttpResponse('Month and year parameters are required.')
    else:
        # If not an AJAX request, render the default template
        current_month = datetime.today().month
        current_year = datetime.today().year
        default_reports = Attendance.objects.filter(
            date__year=current_year,
            date__month=current_month
        )

        return render(request, 'hradmin/employee_reports.html', {'default_reports': default_reports})




@login_required
def download_reports_csv(request):
    if not request.user.is_superuser:
        return redirect('logout')
    # Get month and year parameters from the request
    requested_month = request.GET.get('month')
    requested_year = request.GET.get('year')

    # Validate and convert parameters to integers
    try:
        requested_month = int(requested_month)
        requested_year = int(requested_year)
    except (ValueError, TypeError):
        return HttpResponse('Invalid month or year.', status=400)

    # Filter reports based on requested month and year
    reports = Attendance.objects.filter(
        date__year=requested_year,
        date__month=requested_month
    ).order_by('employee_id')

    # Prepare response as CSV file
    response = HttpResponse(content_type='text/csv')
    filename = f"employee_reports_{requested_year}_{requested_month}.csv"
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    # Create CSV writer
    writer = csv.writer(response)

    # Write header row
    writer.writerow(['Employee Name', 'Employee ID', 'Date', 'Time', 'Status', 'Comments'])

    # Write data rows
    for report in reports:
        writer.writerow([
            report.employee.name,
            report.employee_id,
            report.date,
            report.time,
            report.status,
            report.comments
        ])

    return response
