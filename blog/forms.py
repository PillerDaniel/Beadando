from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text','hirdetesleirasa','price','image', 'allapot', 'kivitel','evjarat', 'kmora', 'szemelyek', 'ajtok', 'karpit','sajattomeg', 'teljestomeg','szin',
         'csomagtarto', 'klima', 'uzemanyag', 'kobcenti', 'kw', 'le', 'henger', 'hajtas', 'sebessegvalto','muszaki', 'okmanyok', 'gumimeret')
        labels ={
            'title': 'Autó pontos megnevezése:',
            'text': 'Leírás:',
            'price':'Az autó ára:',
            'image': 'Fénykép az autóról:',
            'allapot':'Az autó állapota',
            'kivitel':'Kivitel:',
            'evjarat':'Évjárat:',
            'kmora': 'Kilóméteróra állása:',
            'szemelyek': 'Szállítható személyek száma:',
            'ajtok':'Ajtók száma:',
            'karpit':'kárpit színe:',
            'szin' :'Az autó színe:',
            'sajattomeg':'Az autó saját tömege:',
            'teljestomeg':'Az autó teljes tömege:',
            'csomagtarto':'Csomagtartó mérete:',
            'klima':'Klima fajtája:',
            'uzemanyag' : 'Üzemanyag:',
            'kobcenti': 'A motor hengerürtartalma:',
            'kw': 'A motor teljesítménye(KW):',
            'le':'A motor teljesítménye(LE):',
            'henger': 'Henger elrendezése:',
            'hajtas': 'Az autó hajtása:',
            'sebessegvalto':'Sebességváltó:',
            'okmanyok': 'Okmányok:',
            'muszaki':'Müszaki vizsga érvényessége:',
            'gumimeret':'Gumi mérete:',
            'hirdetesleirasa':'A hírdetés leírása:',
        }