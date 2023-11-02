/*Autor: Diego Leon Govea Ortiz
Materia: Seminario estructura de Datos
Actividad 02: Cadenas*/
#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int Concatenar(char* pszInOut, char* pszIn);

int Concatenar(char* pszInOut, char* pszIn){
    int A=strlen(pszInOut);
    int B=strlen(pszIn);
    int C=A+B;

    int i;

    for(i=0;i<C+1;i++){
        if(i<=A-1){
            pszInOut[i]=pszInOut[i];
        }else{
            pszInOut[i]=pszIn[i-A];
        }
    }
    cout<<pszInOut;
}

main(){
    char first[]="Diego",last[]="Govea";
    Concatenar(first,last);

}
