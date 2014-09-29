a = 372.7;
b = -3.962;
c = 99.51;
d = -0.6113;

fitted_curve = @(V) a*exp(b*V) + c*exp(d*V);

actual_distance = data(:,1);
actual_voltage = data(:,2);
expected_distance = fitted_curve(actual_voltage);

plot(actual_distance, expected_distance, 'o');