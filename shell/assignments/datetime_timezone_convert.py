from datetime import datetime
from pytz import timezone


UTC = timezone('UTC')
WAW = timezone('Europe/Warsaw')
BAIKONUR = timezone('Asia/Almaty')


gagarin = 'April 12, 1961 2:07 local time'
gagarin = datetime.strptime(gagarin, '%B %d, %Y %H:%M local time')
gagarin = BAIKONUR.localize(gagarin)

print('Gagarin [UTC]', gagarin.astimezone(UTC))
print('Gagarin [WAW]', gagarin.astimezone(WAW))


armstrong = '"07/21/69 2:56:15 AM UTC"'
armstrong = datetime.strptime(armstrong, '"%m/%d/%y %I:%M:%S %p %Z"')
armstrong = UTC.localize(armstrong)

print('Armstrong [UTC]', armstrong)
print('Armstrong [WAW]', armstrong.astimezone(WAW))
