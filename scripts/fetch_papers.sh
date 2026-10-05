#!/usr/bin/env bash
# 下载 papers/references.bib 中有合法免费全文的论文 PDF 到 papers/pdf/。
#
# 用法（在仓库根目录运行）：
#   bash scripts/fetch_papers.sh          # 下载全部
#   bash scripts/fetch_papers.sh wohlin2014guidelines ralph2022paving   # 只下载指定条目
#
# 说明：
# - 文件名使用 BibTeX 的 key，方便和 references.bib 对应。
# - papers/pdf/ 已加入 .gitignore，PDF 默认不进入仓库（版权各不相同，见 papers/README.md）。
# - 已存在且是有效 PDF 的文件会跳过。
# - 付费论文不在这里，见 papers/README.md 的"待获取"。

set -u
cd "$(dirname "$0")/.."
OUT="papers/pdf"
mkdir -p "$OUT"

# key|url
PAPERS=(
  # 质量标准与报告规范
  "ralph2020empirical|https://arxiv.org/pdf/2010.03525"
  "baltes2026guidelines|https://arxiv.org/pdf/2508.15503"
  "moher2009prisma|https://journals.plos.org/plosmedicine/article/file?id=10.1371/journal.pmed.1000097&type=printable"
  "page2021prisma|https://www.bmj.com/content/372/bmj.n71.full.pdf"
  "kapoor2024reforms|https://www.science.org/doi/pdf/10.1126/sciadv.adk3452"
  # SLR 与映射研究
  "kitchenham2007guidelines|https://legacyfileshare.elsevier.com/promis_misc/525444systematicreviewsguide.pdf"
  "petersen2008systematic|https://www.cse.chalmers.se/~feldt/publications/petersen_ease08_sysmap_studies_in_se.pdf"
  "wohlin2014guidelines|https://www.wohlin.eu/ease14.pdf"
  "wohlin2022successful|https://arxiv.org/pdf/2307.02612"
  "ralph2022paving|https://arxiv.org/pdf/2205.01163"
  # 复现研究
  "carver2010towards|https://carver.cs.ua.edu/Papers/Conference/2010/2010_RESER.pdf"
  # 数据挖掘研究
  "bird2009promises|https://microsoft.com/en-us/research/wp-content/uploads/2016/02/bird2009ppm.pdf"
  "herzig2013bug|https://www.st.cs.uni-saarland.de/publications/files/herzig-icse-2013.pdf"
  "kalliamvakou2014promises|https://kblincoe.github.io/publications/2014_MSR_Promises_Perils.pdf"
  "kalliamvakou2016indepth|https://kblincoe.github.io/publications/2015_EMSE_GitHubPerils.pdf"
  # 工具与模型评测
  "klees2018evaluating|https://arxiv.org/pdf/1808.09700"
  "vanderkouwe2019sok|https://trustworthy.systems/publications/full_text/vanderKouwe_HABG_19.pdf"
  "arp2022dos|https://arxiv.org/pdf/2010.09470"
  # 实证方法通用
  "runeson2009guidelines|https://link.springer.com/content/pdf/10.1007/s10664-008-9102-8.pdf"
  # 综述类论文列表的配套论文（预印本）
  "zhang2026survey|https://arxiv.org/pdf/2312.15223"
  "zhang2024unifying|https://arxiv.org/pdf/2311.07989"
  # 经典文章
  "erren2007ten|https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.0030213&type=printable"
)

want=("$@")
ok=0; skip=0; fail=0; failed=()

for entry in "${PAPERS[@]}"; do
  key="${entry%%|*}"; url="${entry#*|}"
  if [ ${#want[@]} -gt 0 ] && [[ ! " ${want[*]} " =~ " ${key} " ]]; then continue; fi
  dest="$OUT/$key.pdf"
  if [ -s "$dest" ] && head -c 4 "$dest" | grep -q '%PDF'; then
    echo "跳过  $key（已存在）"; skip=$((skip+1)); continue
  fi
  tmp="$dest.part"
  if curl -fsSL --retry 2 --max-time 120 -A "Mozilla/5.0 (merevo-resources fetch script)" -o "$tmp" "$url" \
     && head -c 4 "$tmp" | grep -q '%PDF'; then
    mv "$tmp" "$dest"; echo "完成  $key"; ok=$((ok+1))
  else
    rm -f "$tmp"; echo "失败  $key  <- $url"; fail=$((fail+1)); failed+=("$key")
  fi
done

echo
echo "下载 $ok 篇，跳过 $skip 篇，失败 $fail 篇。"
if [ $fail -gt 0 ]; then
  echo "失败的条目可以用浏览器打开 papers/README.md 中的链接手动下载，保存为 papers/pdf/<key>.pdf："
  printf '  %s\n' "${failed[@]}"
fi
