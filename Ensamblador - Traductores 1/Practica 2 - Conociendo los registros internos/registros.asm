name "registros"

; este programa imprime dos mensajes en la pantall
; escribiendo directamente en la memoria de video.
; en la memoria vga: el primer byte es el caracter ascii,
; el siguiente byte son los atributos del caracter.
; los atributos del caracter es un valor de 8 bits,
; los 4 bits altos ponen el color del fondo
; y los 4 bits bajos ponen el color de la letra.

; hex    bin        color
; 
; 0      0000      black
; 1      0001      blue
; 2      0010      green
; 3      0011      cyan
; 4      0100      red
; 5      0101      magenta
; 6      0110      brown
; 7      0111      light gray
; 8      1000      dark gray
; 9      1001      light blue
; a      1010      light green
; b      1011      light cyan
; c      1100      light red
; d      1101      light magenta
; e      1110      yellow
; f      1111      white
 


org 100h

	mov al, 1
	mov bh, 0  
	;Mensaje uno
	mov bl, 1111_1001b
	mov cx, msg2 - offset msg1 ; calcula el tamano del mensaje. 
	mov dl, 3
	mov dh, 11
	mov bp, offset msg1
	mov ah, 13h
	int 10h  
	
	
	
	;Mensaje dos     
	mov bl, 1111_1100b
	mov cx, msg3 - offset msg2  
	mov dl, 28
	mov dh, 13
	mov bp, offset msg2
	mov ah, 13h
	int 10h
	 
	
	;mensaje tres
	
	mov bl, 1110_0101b
	mov cx, msgend - offset msg3 ; calcula el tamano del mensaje. 
	mov dl, 28
	mov dh, 15
	mov bp, offset msg3
	mov ah, 13h
	int 10h 
	  
	
	jmp msgend 
	
msg1    db "Seccion D01, seminario de solucion de problemas de traductores de lenguaje 1"
msg2    db "Edificio Alpha: Aula 8" 
msg3    db "Diego Leon Govea Ortiz"

msgend: 
        mov dx,0xD318 ;16 bits mas significativos del codigo de alumno ;221349925  
        mov cx,0x8825 ;16 bits menos significativos del codigo de alumno ;221349925   ;1101 0011 0001 1000 1000 0010 0101            
        mov bx,0x1499 ;16 bits mas significativos del NRC del curso
        mov ah,0 
        
        int 16h
        mov ax,0x4996 ;16 bits menos significativos del NRC del curso ;84374 ;0001 0100 1001 1001 0110 
        int 20h 
        
        
