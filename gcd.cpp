#include<iostream>
using namespace std;


int gcd(int a,int b){
    while(a!=b){
        if(a>b){
            a-=b;
        }
        else{
            b-=a;
        }
    }
    return a;
}

int main(){
    int a,b;
    cout<<"enter the two nos to take gcd of : ";
    cin>>a>>b;
    cout<<"gcd = "<<gcd(a,b);
}
