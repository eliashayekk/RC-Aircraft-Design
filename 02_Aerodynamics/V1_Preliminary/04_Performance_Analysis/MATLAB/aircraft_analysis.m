w = m * g;
V = sqrt((2* w) / (rho * wing_area * Cltrim));

fprintf("the speed is: %.3f \n" , V);

AD = Cltrim / Cdtrim;

fprintf("The AD is equal to %.3f.", AD);

speed = 4:0.1:20;

Clreq = (2 * w) ./ (rho .* speed.^2 .*wing_area);


plot(speed,Clreq)
xlabel('Speed (m/s)')
ylabel('Required Lift Coefficient')
title('Required Lift Coefficient vs Speed')
grid on
hold on
yline(1.33)
xline(5.522)
xline(9.182)
yline(0.481)
plot(speed, Clreq, 'LineWidth', 1.5)
hold on

yline(Clmax, '--', 'CL max')
plot(5.522, 1.33, 'o', 'MarkerSize', 8)
plot(9.182, 0.481, 'o', 'MarkerSize', 8)

text(5.522, 1.33, '  Stall')
text(9.182, 0.481, '  Trim')

xlabel('Speed (m/s)')
ylabel('Required Lift Coefficient')
title('Required Lift Coefficient vs Speed')
grid on

legend('Required CL', 'CL max', 'Stall point', 'Trim point')


T = readtable('T1-6_0 m_s-VLM1.csv'); 

alpha = T{1:end,1};
CL = T{1:end,3};
Cm= T{1:end,9};
figure
plot(alpha,CL)
grid on

xlabel('Angle of Attack (deg)')
ylabel('Lift Coefficient CL')
title('CL vs Angle of Attack')

figure
plot(alpha, Cm)
grid on

xlabel('Angle of Attack (deg)')
ylabel("Pitching Moment Coefficient Cm")
title ("Cm vs alpha")

