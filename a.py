f = open('nothing.html','w')
t=input("Enter your title :")
h=input("Please write heading :")
b=input("Bold text :")
i=input("Italic text :")
u=input("Underlined text :")
f.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>%s</title>
</head>
<body>
    <h1>%s</h1>
    <b>%s</b>
    <i>%s</i>
    <u>%s</u>
</body>
</html>
""" %(t,h,b,i,u))
f.close()