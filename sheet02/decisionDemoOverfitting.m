load fisheriris.mat;
tc = fitctree(meas,species);%,'CrossVal','on');
sum(strcmp(predict(tc,meas),species))/length(meas)
tc2 = prune(tc,'Level',2);
sum(strcmp(predict(tc2,meas),species))/length(meas)
view(tc2,'Mode','graph')
