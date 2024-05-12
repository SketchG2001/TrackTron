from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime, time as datetime_time

from employee.models import Attendance


# 22.6876, 75.827124
# 22.7049472, 75.9005184
# 22.6876039, 75.8271282
# 22.6875937, 75.8271162
@login_required
def presence(request):
    if request.method == 'POST':
        username = request.POST['username']
        employee_id = request.POST['employee_id']
        date = request.POST['date']
        time = request.POST['time']
        location = request.POST['location']
        status = request.POST['status']
        comments = request.POST['comments']
        print(username, employee_id, date, time, location, status, comments)
        allowed_locations = [
            '22.6876, 75.827124',
            '22.7049472, 75.9005184',
            '22.6876039, 75.8271282',
            '22.6875937, 75.8271162',
            '22.6875979, 75.8271244',
            '22.6875979, 75.8271244',
            '22.6876017, 75.8271246',
            '22.6876021, 75.8271295'
        ]
        location_is_valid = False
        # if location not in allowed_locations:
        #     messages.error(request, 'Invalid location')
        #     return render(request,'employee/presence.html')
        # else:
        #     location_is_valid = True

        if username != request.user.username or employee_id != str(request.user.id):
            messages.error(request, 'Invalid username')
            return render(request, 'employee/presence.html')
        print(username)
        current_datetime = datetime.now()
        current_date = current_datetime.date()
        current_time = current_datetime.time()

        print(current_time, current_date)

        attendance_cutoff_time = datetime_time(5, 40, 0)
        existing_attendance = Attendance.objects.filter(employee_id=request.user.id, date=current_date).first()
        if existing_attendance:
            messages.error(request, 'Attendance already recorded for today')
            return redirect('dashboard')
        print('none', existing_attendance)

        if date != str(current_date):
            messages.error(request, f'Invalid date {date}')
            print('invalid date')
            return render(request, 'employee/presence.html')
        print(date)
        location_is_valid = True
        if current_time > attendance_cutoff_time:
            # Mark the employee as absent if attendance is not recorded by the cutoff time
            present_emp = Attendance.objects.create(
                employee_id=employee_id,
                date=date,
                time=time,  # Time is not recorded because attendance is late
                location=location_is_valid,
                status='Late',
                comments='Attendance not recorded on time'
            )
            present_emp.save()
            messages.warning(request, 'Attendance marked as absent (recorded late)')
            return redirect('dashboard')

        if location_is_valid:
            present_emp = Attendance.objects.create(
                employee_id=employee_id,
                date=date,
                time=time,
                location=location_is_valid,
                status=status,
                comments=comments
            )
            present_emp.save()
            messages.success(request, 'Attendance recorded successfully')
            return redirect('dashboard')

    username = request.user.username
    name = request.user.name
    emp_id = request.user.id
    return render(request, 'employee/presence.html', {'name': name, 'username': username, 'emp_id': emp_id})
