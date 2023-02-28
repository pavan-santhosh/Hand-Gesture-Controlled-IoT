#include<iostream>
#include<math.h>
#include<vector>

/* Define function here */
#define f(x) 1/(1+x+y)

using namespace std;
int main()
{
    int x=0, y=0;
    int upper_limit_x = 2.8;
    int lower_limit_x = 2;
    int upper_limit_y = 1.4;
    int lower_limit_y = 1;
    int interval = 4;
    int h = (upper_limit_x-lower_limit_x)/interval;
    int k = (upper_limit_y-lower_limit_y)/interval;
    vector<int> L;

    while(lower_limit_y <= (upper_limit_y + 0.1)){
        vector<int> l;
        l.insert(l.begin(), lower_limit_y);
        while(lower_limit_x <= (upper_limit_x+0.2)){
            int f = 1/(1+lower_limit_x+lower_limit_y);
            l.insert(l.end(), f);
            lower_limit_x += 0.2;
        }
        L.insert(L.end(), l.begin(), l.end());
        lower_limit_x = 2;
        lower_limit_y += 0.1;
    }
    L.insert();


 float lower, upper, integration=0.0, stepSize, k;
 int i, subInterval;

 /* Input */
 cout<<"Enter lower limit of integration: ";
 cin>>lower;
 cout<<"Enter upper limit of integration: ";
 cin>>upper;
 cout<<"Enter number of sub intervals: ";
 cin>>subInterval;

 /* Calculation */

 /* Finding step size */
 stepSize = (upper - lower)/subInterval;

 /* Finding Integration Value */
 integration = f(lower) + f(upper);

 for(i=1; i<= subInterval-1; i++)
 {
  k = lower + i*stepSize;
  integration = integration + 2 * (f(k));
 }

 integration = integration * stepSize/2;

 cout<< endl<<"Required value of integration is: "<< integration;

 return 0;
}