from django.db.models.signals import post_save
from django.dispatch import receiver
from employee.models import LeaveRequest, Attendance


@receiver(post_save, sender=LeaveRequest)
def handle_leave_approval(sender, instance, created, **kwargs):
    if not created and instance.status == 'approved':
        # Find all attendance records within the leave period for the employee
        attendances = Attendance.objects.filter(
            employee=instance.employee,
            date__range=[instance.start_date, instance.end_date]
        )

        # Update attendance records to indicate 'on leave'
        for attendance in attendances:
            attendance.on_leave = True
            attendance.status = 'on leave'
            attendance.comments = 'On approved leave'
            attendance.save()
