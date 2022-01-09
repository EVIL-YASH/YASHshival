#Writing in file 
with open("text.txt", "w",encoding='utf-8')as f:
    f.write("Jai Hind Dosto")
    f.close()
    f = open("text.txt", "r")
print(f.read())
##Reading file
f = open('text.txt','r',encoding='utf-8')
print(f.read())
# closing opened file
f = open("text.txt", "r",encoding='utf-8')
print(f.read())
f.close()


##Reading file
f = open('text.txt','r')
print(f.read())
#Writing in file
f = open("text.txt", "w")
f.write("Shaamein malang see Raatein surang see Waadi udaan pe hi na jaane kyun Ilahi mera jee aaye aaye Ilahi mera jee aaye aaye.. Kal pe sawaal hai Jeena filhal hai Khanabadoshiyon pe hi jaane kyun Ilahi mera jee aaye aaye Ilahi mera jee aaye aaye.. Mera falsafa Kandhe pe mera Basta chala main jahaan Le chala mujhe rastaa Boondon pe nahin Gehre samandar pe Oou O.. O.. Ilahi mera jee aaye aaye Ilahi mera jee aaye aayevShaamein malang si Raatein surang si Waadi udaan pe hi na jaane kyoon Ilaahi mera jee aaye aaye Ilaahi mera jee aaye aaye...")
f.close()
f = open("text.txt", "r")
print(f.read())
# closing opened file
f = open("text.txt", "r")
print(f.read())
f.close()


