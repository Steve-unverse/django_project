from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def first_view(response):
    https = '''
    <h1> assalomu alekum </h1>
    <a href="last_view">python</a>
    '''
    return HttpResponse(https)
def last_view(response):
    https = '''
        <h1>Ma'lumot</h1>
        <a href="../"><h2>Home</h2></a>
    <table>
        <tr>
            <td colspan="3">F.I.SH</td>
            <td colspan="1">Viloyat</td>
            <td colspan="3">Tug'ulgan yili</td>
        </tr>
        <tr>
            <td style="background-color: yellow;">Zaripova</td>
            <td style="background-color: yellow;">Muqaddas</td>
            <td style="background-color: yellow;">Jumaniyozovna</td>
            <td style="background-color: yellow;">Samarqand</td>
            <td style="background-color: yellow;">1972 yil</td>
            <td style="background-color: yellow;">7</td>
            <td style="background-color: yellow;">aprel</td>
        </tr>
        <tr>
            <td style="background-color: yellow;">Yusupova</td>
            <td style="background-color: yellow;">Dilfuza</td>
            <td style="background-color: yellow;">Aminovna</td>
            <td style="background-color: yellow;">Farg'ona</td>
            <td style="background-color: yellow;">1968 yil</td>
            <td style="background-color: yellow;">7</td>
            <td style="background-color: yellow;">may</td>
        </tr>
    </table>    
    '''
    return HttpResponse(https)