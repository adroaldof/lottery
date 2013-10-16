import datetime
import errno
import os
import urllib2
import zipfile

from bs4 import BeautifulSoup
from StringIO import StringIO

from django.conf import settings
from megasena.models import Concourse, Raffle


def convert_str_to_date(string):
    string = "%s-%s-%s" % (string[6:10], string[3:5], string[0:2])
    return datetime.datetime.strptime(string, '%Y-%m-%d').date()


def translate(string):
    if (string == "SIM"):
        return True
    return False


def convert_str_to_float(string):
    replaced = string.replace('.', '')
    replaced = replaced.replace(',', '.')
    return float(replaced)


def parse_data(page):
    soup = BeautifulSoup(page)
    table = soup.find('table')
    tag = False

    for row in table.findAll('tr'):
        col = row.findAll('td')
        if col:
            q1 = int(col[0].string.strip())
            q2 = convert_str_to_date(col[1].string.strip())
            q3 = int(col[2].string.strip())
            q4 = int(col[3].string.strip())
            q5 = int(col[4].string.strip())
            q6 = int(col[5].string.strip())
            q7 = int(col[6].string.strip())
            q8 = int(col[7].string.strip())
            q9 = convert_str_to_float(col[8].string.strip())
            q10 = int(col[9].string.strip())
            q11 = convert_str_to_float(col[10].string.strip())
            q12 = int(col[11].string.strip())
            q13 = convert_str_to_float(col[12].string.strip())
            q14 = int(col[13].string.strip())
            q15 = convert_str_to_float(col[14].string.strip())
            q16 = translate(col[15].string.strip())
            q17 = convert_str_to_float(col[16].string.strip())
            q18 = convert_str_to_float(col[17].string.strip())
            q19 = convert_str_to_float(col[18].string.strip())

            concourse, created = Concourse.objects.get_or_create(number=q1)
            megasena, created = Raffle.objects.get_or_create(
                number=concourse,
                raffle_date=q2,
                n01=q3,
                n02=q4,
                n03=q5,
                n04=q6,
                n05=q7,
                n06=q8,
                collected_amount=q9,
                sena_winners=q10,
                sena_share=q11,
                quina_winners=q12,
                quina_share=q13,
                quadra_winners=q14,
                quadra_share=q15,
                accumulated_status=q16,
                accumulated_value=q17,
                prize_next=q18,
                prize_turnaround=q19
            )

            if created:
                tag = True

            megasena.save()

    return tag


def open_local_file():
    system_path = settings.MEDIA_ROOT
    file_path = '/megasena/'
    filepath = system_path + file_path + 'D_mgsasc.zip'
    file = urllib2.urlopen('file://' + filepath)

    try:
        os.remove(filepath)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise e.errno

    unzip_file(file)


def unzip_file(file):
    uncompressed = None

    try:
        files = zipfile.ZipFile(StringIO(file.read()))
        filename = ''
        for file in files.infolist():
            if file.filename.endswith('.htm'):
                filename = file.filename
        uncompressed = files.open(filename)
    except:
        pass

    parse_data(uncompressed)
