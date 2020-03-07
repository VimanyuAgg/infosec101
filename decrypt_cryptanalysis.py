# Main file of the Python 3 program.
from collections import Counter
import re

text = """
hm al, mo tmh hm al, huvh gn hul jzlnhgmt:
qulhulo 'hgn tmaxlo gt hul cgty hm nzrrlo
hul nxgtsn vty voomqn mr mzhovslmzn rmohztl,
mo hm hvel vocn vsvgtnh v nlv mr homzaxln
vty ak mppmngts lty hulc?
hm ygl: hm nxllp;
tm cmol; vty, ak v nxllp hm nvk ql lty
hul ulvoh-vwul vty hul humznvty tvhzovx numwen
huvh rxlnu gn ulgo hm, 'hgn v wmtnzccvhgmt
yldmzhxk hm al qgnu'y. hm ygl, hm nxllp;
hm nxllp: plowuvtwl hm yolvc: vk, hulol'n hul oza;
rmo gt huvh nxllp mr ylvhu quvh yolvcn cvk wmcl
qult ql uvdl nuzrrxly mrr hugn cmohvx wmgx,
cznh sgdl zn pvznl
"""
print(Counter(text))
text = text.replace('l','_e')
text = text.replace('h','_t')
text = text.replace('m','_o')
text = text.replace('a','_b')
text = re.sub('(?<!_)o','_r', text)
text = re.sub('(?<!_)t','_n', text)
text = re.sub('(?<!_)u','_h', text)
text = re.sub('(?<!_)v','_a', text)
text = re.sub('(?<!_)g','_i', text)
text = re.sub('(?<!_)n','_s', text)
text = re.sub('(?<!_)j','_q', text)
text = re.sub('(?<!_)z','_u', text)
text = re.sub('(?<!_)q','_w', text)
text = re.sub('(?<!_)s','_g', text)
text = re.sub('(?<!_)r','_f', text)
text = re.sub('(?<!_)x','_l', text)
text = re.sub('(?<!_)c','_m', text)
text = re.sub('(?<!_)y','_d', text)
text = re.sub('(?<!_)e','_k', text)
text = re.sub('(?<!_)p','_p', text)
text = re.sub('(?<!_)w','_c', text)
text = re.sub('(?<!_)d','_v', text)
text = re.sub('(?<!_)k','_y', text)
print(text)

# Below helps when figuring out some missing decryptions as it replaces unknowns with # sign.
# To see them in action, just comment out a few regex substitution lines
text = re.sub('(?<!_)[a-z]','#', text)

print(text.replace("_",""))
