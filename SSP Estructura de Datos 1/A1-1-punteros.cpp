/*Autor: Diego Leon Govea Ortiz
Materia: Estructura de Datos
Actividad 01: Tipos de dato primitivos y Tipos de Dato Estructurado*/

#include <iostream>

using namespace std;

int main(){
    int iX,iY,*pA;
    iX=5;
    iY=10;

    pA=&iX;
    cout<<iX<<endl;
    cout<<*pA<<endl;
    cout<<&iX<<endl;
    cout<<pA<<endl;


    pA=&iY;
    cout<<iY<<endl;
    cout<<*pA<<endl;
    cout<<&iY<<endl;
    cout<<pA<<endl;

}
