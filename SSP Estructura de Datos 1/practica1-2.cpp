/*Autor: Diego Leon Govea Ortiz
Materia: Estructura de Datos
Actividad 01: Tipos de dato primitivos y Tipos de Dato Estructurado*/

#include <iostream>

using namespace std;

int Potencia(int iBase, int iExp);
void Potencia2(int* pBase, int iExp);

int Potencia(int iBase, int iExp){
    int resultado=1,i;
    for(i=0;i<iExp;i++){
        resultado=iBase*resultado;
    }

    return resultado;
}

void Potencia2(int* pBase, int iExp){
    int i,resultado=1;
    for(i=0;i<iExp;i++){
        resultado=*pBase*resultado;
    }
    *pBase=resultado;

}

int main(){
    int base;
    int* x;

    base=10;
    x=&base;
    cout<<Potencia(8,3)<<endl;
    Potencia2(x,3);
    cout<<base;

}
