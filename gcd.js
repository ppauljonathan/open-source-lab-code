function gcd(a,b){
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

var a=window.prompt("no1 : ");
var b=window.prompt("no2 : ");

alert(gcd(a,b));
