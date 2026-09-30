#include<stdio.h>
#include<string.h>
#include<ctype.h>
int isp(char item);
void output(char item);
void push(char item);
char pop(void);
void quad(void);
char exp[20];
char res[20];
char a[20],opr[20],opd1[20],opd2[20],result[20];
int st[20],value[20];
int top=0,z=0,i=0,op1,op2,k,j,p,l;
char x,item;

void main()
{
printf("Enter the infix expression: ");
gets(exp);
l=strlen(exp);
push('#');
while((item=exp[i])!='\0')
{
if(isalpha(exp[i]))
output(item);
else if(item=='+'||item=='-'||item=='*'||item=='/'||item=='^')
push(item);
else if(item=='(')
push(item);
else if(item==')')
{
while((x=pop())!='(')
output(x);
}
else if(isp(x=pop())<isp(item))
{
push(x);
push(item);
}
else
{
output(x);
push(item);
}
i++;
}
while((x=pop())!='#')
output(x);
printf("Postfix expression: ");
puts(res);
quad();
}

int isp(char item)
{
if((item=='+')||(item=='-'))
return(1);
else if((item=='*')||(item=='/'))
return(2);
else if((item=='^'))
return(3);
else
return(0);
}
void output(char item)
{
res[z++]=item;
}
void push(char item)
{
a[++top]=item; }
char pop(void)
{
item=a[top--];
return(item); }
void quad()
{
int i,x=0;
char m,n,p,temp,str1[5],str2[5];
printf("\noperator\top1\top2\tresult\n");
printf("----------------------------");
for(i=0;i<l;i++)
{
if(isalnum(res[i]))
{
push(res[i]); }
else
{
if(isalpha(m=pop()))
{
str1[0]=m;
str1[1]='\0'; }
else
{
str1[0]='t';
str1[1]=m;
str1[2]='\0'; }
if(isalpha(n=pop()))
{
str2[0]=n;
str2[1]='\0'; }
else
{ str2[2]='\0'; }
x++;
printf("\n%c\t\t%s\t%s\tt%d\n",res[i],str2,str1,x);
temp=x+'0';
push(temp);
} } }
