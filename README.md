# Jetson TegraStats Plotter

使用 NVIDIA `tegrastats` 記錄G1 Jetson Orin CPU、GPU、RAM 等系統資源，並透過 Python 解析後使用 Gnuplot 繪圖。

![tegrastat](./jetsonStats.png)

## 1. 開始記錄

每 100 ms 記錄一次：

```bash
tegrastats --interval 100 > tegrastats_$(date +%Y%m%d_%H%M%S).log 2>&1 &
```

例如會產生：

```text
tegrastats_20260821_135119.log
```

## 2. 停止記錄

```bash
pkill tegrastats
```

確認是否已停止：

```bash
pgrep -a tegrastats
```

若沒有輸出，代表已停止。

## 3. 解析 Log

```bash
python tegra_plotter.py --log_path tegrastats_20260821_135119.log
```

程式會解析：

* GPU 使用率
* CPU0 ~ CPU7 使用率
* RAM 使用量(Unified memory)
* CPU / GPU 溫度

並產生供 Gnuplot 使用的：

```text
tegra_stats.dat
```

## 4. 繪圖

```bash
gnuplot -persist plot.gp
```

目前圖表包含：

* GPU Usage
* CPU0 ~ CPU7 Usage
* RAM Usage

## 安裝 Gnuplot

Ubuntu / Jetson：

```bash
sudo apt update
sudo apt install gnuplot
```

Headless 環境：

```bash
sudo apt install gnuplot-nox
```

## Workflow

```text
tegrastats
    ↓
*.log
    ↓
tegra_plotter.py
    ↓
tegra_stats.dat
    ↓
plot.gp
    ↓
GPU / CPU / RAM Plot
```

## Example

```bash
tegrastats --interval 10 > tegrastats_$(date +%Y%m%d_%H%M%S).log 2>&1 &

pkill tegrastats

python tegra_plotter.py --log_path tegrastats_20260821_135119.log

gnuplot -persist plot.gp
```

> `--interval 10` 表示每 10 ms 取樣一次，也就是 100 Hz。

