import urllib.parse

def main():
  num = input("ingresa numero de wsp (de esta forma 569xxxxxxxx): ")
  msg = input("ingresa el mensaje: ") 

  url="https://wa.me/" + num.strip().replace(" ", "").replace("+", "") + "/?text=" + (urllib.parse.quote(msg))

  print('El link para el wsp es: "' + url + '"')

if __name__=='__main__':
  main();    