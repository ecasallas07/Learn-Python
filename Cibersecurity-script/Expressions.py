import re

#return  a list of matches  to a regular  expression
re.findall()

email_log = """
                Email recived  june 2 from  user1@gmail.com.
                Email recived  june 2 from  use2@gmail.com.
                Email recived  june 2 from  invalid_email@gmail.com.
            """
            
print(re.findall("\w+@\w+\ . \w+",email_log))

# EXAMPLES
devices = "r262c36 67bv8fy 41j1u2e r151dm4 1270t3o 42dr56i r15xk9h 2j33krk 253be78 ac742a1 r15u9q5 zh86b2l ii286fq 9x482kt 6oa6m6u x3463ac i4l56nq g07h55q 081qc9t r159r1u"

# Asigna `target_pattern` a un patrón de expresión regular para encontrar las ID de dispositivo que comiencen con "r15"

target_pattern = "r15\w+"


# -----------------------------------------------------------
# EXAMPLE 01
devices1 = "r262c36 67bv8fy 41j1u2e r151dm4 1270t3o 42dr56i r15xk9h 2j33krk 253be78 ac742a1 r15u9q5 zh86b2l ii286fq 9x482kt 6oa6m6u x3463ac i4l56nq g07h55q 081qc9t r159r1u"

# Asigna `target_pattern` a un patrón de expresión regular para encontrar las ID de dispositivo que comiencen con "r15"

target_pattern = "r15\w+"

# Utiliza `re.findall()` para encontrar las ID de dispositivo que comienzan con "r15" y muestra los resultados

print(re.findall(target_pattern, devices1))

#--------------------------------------------------------
#EXAMPLE 02
log_file = "eraab 2022-05-10 6:03:41 192.168.152.148 \niuduike 2022-05-09 6:46:40 192.168.22.115 \nsmartell 2022-05-09 19:30:32 192.168.190.178 \narutley 2022-05-12 17:00:59 1923.1689.3.24 \nrjensen 2022-05-11 0:59:26 192.168.213.128 \naestrada 2022-05-09 19:28:12 1924.1680.27.57 \nasundara 2022-05-11 18:38:07 192.168.96.200 \ndkot 2022-05-12 10:52:00 1921.168.1283.75 \nabernard 2022-05-12 23:38:46 19245.168.2345.49 \ncjackson 2022-05-12 19:36:42 192.168.247.153 \njclark 2022-05-10 10:48:02 192.168.174.117 \nalevitsk 2022-05-08 12:09:10 192.16874.1390.176 \njrafael 2022-05-10 22:40:01 192.168.148.115 \nyappiah 2022-05-12 10:37:22 192.168.103.10654 \ndaquino 2022-05-08 7:02:35 192.168.168.144"

# Asigna a `pattern` un patrón de expresión regular que coincida con las direcciones IP de la forma xxx.xxx.xxx.xxx
pattern = "\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d"
