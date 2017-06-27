clc;
activeP=.875e6;
for j=1:26
    sim('sherikkum_model.mdl');
    a=neg_seq_voltage(201:end,2);
    [C,L] = wavedec(a,5,'db4');
    i=1;
    count=L(1);
    while i<=5
        data=C(count+1:count+L(i+1));
        E(j,i)=norm(data,2);
        SD(j,i)=std(data);
        count=count+L(i+1);
        i=i+1;
    end
    activeP=activeP+.035e6;
    fprintf('Iterarion Number : %d \n',j);
end
fprintf('\n\n TABLE \n\n');
Loading=.875:.035:1.75;
Loading=Loading';
T = table(Loading,SD,E);
disp(T);



