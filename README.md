# dxheat-alert

[DXHeat](https://dxheat.com/dxc/) is a lovely DX cluster incorporating a heat map showing
band activity based on the totality of spots reported to the cluster.

This script downloads the raw data behind the heatmap and prints a line of text for each band
with a total activity score above a certain threshold, as specified on the command line.

It's designed to be used as a cron job so that any output will generate an email; for example,

    */10 * * * *  python dxheat-alert.py 100

If you're not in Europe, you'll need to edit the URL in the script accordingly.

Obviously any change to DXHeat will probably break this script, but you get what you pay for :-)
