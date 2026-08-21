set terminal qt size 1400,900

set multiplot layout 3,1 title "Jetson System Usage"
set grid
set key outside right

# GPU
set ylabel "GPU (%)"
set autoscale y
unset xlabel
plot "tegra_stats.dat" using 1:2 with lines title "GPU"

# CPU 0~7
set ylabel "CPU (%)"
set autoscale y
plot "tegra_stats.dat" using 1:3 with lines title "CPU0", \
     "" using 1:4 with lines title "CPU1", \
     "" using 1:5 with lines title "CPU2", \
     "" using 1:6 with lines title "CPU3", \
     "" using 1:7 with lines title "CPU4", \
     "" using 1:8 with lines title "CPU5", \
     "" using 1:9 with lines title "CPU6", \
     "" using 1:10 with lines title "CPU7"

# RAM
set ylabel "RAM (MB)"
set xlabel "Time (s)"
set autoscale y
plot "tegra_stats.dat" using 1:11 with lines title "RAM"

unset multiplot
pause mouse close
