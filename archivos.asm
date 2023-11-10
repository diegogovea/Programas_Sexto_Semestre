name "archivos"


include emu8086.inc
org 100h
 jmp inicio 
 archivo1 db 11 dup (0), 0
 archivo2 db 11 dup (0), 0
 linea db 50 dup (0), 0 
 salto db 13, 10
 caracter db "$" 
 contador dw 0x0 
 parcial dw 0x0
 handle dw ?
 handle2 dw ? 
 numerador dw ?
 denominador db 0x0A
 residuo db ?
 cociente db ?
 decimal db 48,48,48,32
 
inicio: 
 GOTOXY 8,4
 PRINT "Seminario de Traductores de lenguajes"
 GOTOXY 8,5 
 PRINT "Daniel Sanchez Zepeda" 
 GOTOXY 8,6 
 PRINT "Digite el nombre del archivo entrada: " 
 xor ax, ax
 lea di,archivo1
  mov dx,11
 call GET_STRING
 GOTOXY 8,7 
 PRINT "Digite el nombre del archivo salida: " 
 xor ax, ax
 lea di,archivo2
 mov dx,11
 call GET_STRING 
 GOTOXY 8,8 
 PRINT "Los archivos se almacenan en C:\emu8086\MyBuild" 
 
 xor ax, ax
 xor dx, dx
 mov al, 0 
 mov dx, offset archivo1 
 mov ah, 3dh 
int 21h
jc err 
 mov handle, ax 
 
 mov cx, 0 ; normal - no attributes. 
 mov dx, offset archivo2
 mov ah, 0x3c
 int 21h
jc errCrear
 mov handle2, ax 
 
 xor bx, bx 
 xor cx, cx
 xor dx, dx
 mov bx, [handle2] 
 mov cx, 0x4
 mov dx, offset decimal 
 mov ah, 40h
 int 21h
 
 mov bx, [handle]
 mov cx, 0x1 
 mov dx, offset caracter
 lea di, linea 
 
leer:
 mov ah, 0x3f ;read from file. 
  int 21h 
 
 cmp ax, 0x0
 jz finArchivo
 xor ax, ax
 mov al, caracter[0] 
 cmp al, 13 
 jz leer
 cmp al, 10 
 jz nuevaLinea
 mov [di], al 
 inc di
 inc contador
 inc parcial
 jmp leer
nuevaLinea: 
 xor ax, ax
 lea di, decimal+2
 mov ax, [contador]
 mov [numerador], ax 
 
convertir:
 call division
 xor ax, ax 
 mov al, [residuo] 
 add al, 48
 mov [di], al
 dec di
 xor ax, ax
 mov al, [cociente]
 mov [numerador], ax
 xor bx, bx
 mov bl, [denominador]
 cmp ax, bx
 jle finDecimal
 jmp convertir 
finDecimal: 
 add al, 48
 mov [di], al
 call escribirLinea
 call limpiarLinea
  mov bx, [handle]
 mov cx, 0x1 
 mov dx, offset caracter
 lea di, linea 
 mov [parcial], 0x0
 jmp leer 
 
 
finArchivo: 
 xor ax, ax
 lea di, decimal+2
 mov ax, [contador]
 mov [numerador], ax 
 
convertirFinal:
 call division
 xor ax, ax 
 mov al, [residuo]
 add al, 48
 mov [di], al
 dec di
 xor ax, ax
 mov al, [cociente]
 mov [numerador], ax
 xor bx, bx
 mov bl, [denominador]
 cmp ax, bx
 jle finArc
 jmp convertirFinal 
finArc:
 add al, 48
 mov [di], al
 call escribirLinea
 jmp fin
 
 
escribirLinea:
 pusha 
 
 xor bx, bx 
 xor cx, cx
xor dx, dx
 mov bx, [handle2] 
 mov cx, [parcial]
 mov dx, offset linea 
 mov ah, 40h
 int 21h 
 
 mov cx, 2
 mov dx, offset salto
 mov ah, 40h
 int 21h
 
 mov cx, 0x4
 mov dx, offset decimal 
 mov ah, 40h
 int 21h
 
 popa 
 ret 
 
limpiarLinea: 
 pusha
 mov cx, [parcial]
 lea si, linea
borrar: 
 mov [si], 0x0 
 inc si
 loop borrar
 popa 
 ret 
 
division:
 pusha
 xor dx, dx
 xor ax, ax
 xor bx, bx
 mov ax, [numerador]
 mov bl, [denominador]
 div bl
 mov [cociente], al
 mov [residuo], ah
 
 popa
 ret 
 
err:
 GOTOXY 8,9 
 PRINT "Error al abrir el archivo" 
 
errCrear:
 GOTOXY 8,10 
 PRINT "Error al crear el archivo de salida" 
 
fin:
 
 xor bx, bx 
 xor ax, ax
 mov bx, [handle]
 mov ah, 0x3e
 int 21h
 
 xor bx, bx 
 xor ax, ax
 mov bx, [handle2]
 mov ah, 0x3e
 int 21h
 
 GOTOXY 8,11 
 PRINT "Los archivos se guardaron exitosamente" 
 
 int 20h
 
 DEFINE_GET_STRING
ret
