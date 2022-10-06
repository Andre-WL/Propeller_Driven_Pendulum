clear variables; clc;
close all;

num = 0.05713502148276807752079714781973*1.9577*57.295779513082320876798154814105;
den = [0.0054 0.0623 0.4541 2.5529 6.4052];
G = tf(num,den);

num_PI = [0.15 1.5];
den_PI = [1 0];
G_PI = tf(num_PI,den_PI);
G_c = G*G_PI;

num_PD = [0.1 1];
den_PD = 1;
G_PD = tf(num_PD,den_PD);

G_PID = G_c*G_PD;

%unity gain PI
% num_PIu = [1 1];
% den_PI = [1 0]; %can be used for all PI denoms
% 
% G_PIu = tf(num_PIu,den_PI);
% 
% G_c1 = G*G_PIu;
% 
% %PI with 6.5rad/s omega_b
% num_PI65 = [0.15625 1];
% G_PI65 = tf(num_PI65, den_PI);
% 
% G_c2 = G*G_PI65;
% 
% %PI with 6.5rad/s omega_b, ki=1.3
% num_PI = [0.203125 1.3];
% 
% G_PI = tf(num_PI,den_PI);
% G_c3 = G*G_PI;

%figures

%root locus
% figure
% hold on
% rlocus(G)
% title('Root locus for propeller driven pendulum')
% hold off

%uncompd bode
%this one is for reading GM and PM
figure
hold on
margin(G)
hold off

figure
hold on
margin(G_c)
hold off

figure
hold on
margin(G_PID)
hold off
% figure
% step(G)
%this one is for figure in report
% figure
% hold on
% magin(G)
% title('Bode plot for propeller driven pendulum')
% hold off

%1rad/s comped bode
%this one is for reading GM and PM
% figure
% hold on
% margin(G_c1)
% hold off
% 
% % figure
% % hold on
% % margin(G_PIu)
% % hold off
% 
% %this one is for figure in report
% % figure
% % hold on
% % magin(G_c1)
% % title('Bode plot with 1rad/s (\omega)_{b} PI')
% % hold off
% 
% %6.5rad/s comped bode
% %this one is for reading GM and PM
% figure
% hold on
% margin(G_c2)
% hold off
% 
% % figure
% % hold on
% % margin(G_PI65)
% % hold off
% 
% %this one is for figure in report
% % figure
% % hold on
% % magin(G_c2)
% % title('Bode plot with 6.5rad/s (\omega)_{b} PI')
% % hold off
% 
% %6.5rad/s comped bode, ki=1.3
% %this one is for reading GM and PM
% figure
% hold on
% margin(G_c3)
% hold off
% 
% % figure
% % hold on
% % margin(G_PI)
% % hold off
% 
% % %this one is for figure in report
% % figure
% % hold on
% % magin(G_c2)
% % title('Bode plot with 6.5rad/s (\omega)_{b} K_{i}=1.3 PI')
% % hold off