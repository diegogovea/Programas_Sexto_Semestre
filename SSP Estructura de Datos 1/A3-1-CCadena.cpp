/*Autor: Diego Leon Govea Ortiz
Practica 3: cCadena
Seminario de Estructura de Datos*/

#include <iostream>
#include<string.h>

using namespace std;

class Ccadena{
    char szBuffer[128];

public:
    void leer();
    void imprimir();

    void ImprimeVetical();
    void ImprimeReves();
    int Cuenta(char cContar);
    int PrimerAparicion(char cBuscar);
    int Concatenar(char* pszIn);
    void Reves();

};

void Ccadena::leer()
{
    cout<<"Escribe una cadena: ";
    cin>>szBuffer;
}

void Ccadena::imprimir()
{
    int i;
    for(i=0;szBuffer[i]!=NULL;i++){
        cout<<szBuffer[i];
    }

}

void Ccadena::ImprimeVetical()
{
    int i;
    for(i=0;szBuffer[i]!=NULL;i++){
        cout<<szBuffer[i]<<endl;
    }

}

void Ccadena::ImprimeReves()
{
    int i;
    for(i=0;szBuffer[i]!=NULL;i++);
    for(i=i-1;szBuffer[i]!=NULL;i--){
        cout<<szBuffer[i];
    }
}

int Ccadena::Cuenta(char cContar)
{
    int i,c=0;

    for(i=0;szBuffer[i]!=NULL;i++){
        if(szBuffer[i]==cContar)c++;
    }

    return c;
}

int Ccadena::PrimerAparicion(char cBuscar)
{
    int i,c=0;

    for(i=0;szBuffer[i]!=NULL;i++){
        if(szBuffer[i]==cBuscar){
            return i;
            break;
        }
    }
	return -1;

}

int Ccadena::Concatenar(char* pszIn)
{
    int A=strlen(szBuffer);
    int B=strlen(pszIn);
    int C=A+B;

    int i;

    for(i=0;i<C+1;i++){
        if(i<=A-1){
            szBuffer[i]=szBuffer[i];
        }else{
            szBuffer[i]=pszIn[i-A];
        }
    }
}

void Ccadena::Reves(){
    int i,j;
    char otraCadena[128];
    for(i=0;szBuffer[i]!=NULL;i++){
        otraCadena[i]=szBuffer[i];
    }
    j=i-1;
    for(i=0,j;szBuffer[j]!=NULL;i++,j--){
        szBuffer[i]=otraCadena[j];
    }
}



int main()
{
    char c='e';
    Ccadena a, b;
    cout << "Bienvenido a programa de cCadena" << endl;
    a.leer(); //Introducir la cadena
    cout<<endl<<endl;

    cout<<"Impresion en horizontal"<<endl;
    a.imprimir();
    cout<<endl<<endl;

    cout<<"Impresion en vertical"<<endl;
    a.ImprimeVetical();
    cout<<endl;

    cout<<"Impresion al reves"<<endl;
    a.ImprimeReves();
    cout<<endl<<endl;

    cout<<"Cuenta de caracteres"<<endl;
    cout<<"El caracter e se repite "<<a.Cuenta(c)<<" veces";
    cout<<endl<<endl;

    cout<<"La primer posicion de la letra e es: "<<a.PrimerAparicion(c)<<endl;
    cout<<endl<<endl;

    cout<<"Concatenar"<<endl;
    a.Concatenar("Diego");
    a.imprimir();
    cout<<endl<<endl;

    cout<<"Reves"<<endl;
    a.Reves();
    a.imprimir();
    cout<<endl<<endl;
    a.ImprimeReves();
    cout<<endl<<endl;

    return 0;
}
