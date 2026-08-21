tegrastats --interval 100 > tegrastats_$(date +%Y%m%d_%H%M%S).log 2>&1 &
pkill tegrastats


python tegra_plotter.py --log_path tegrastats_20260821_135119.log
gnuplot -persist plot.gp

