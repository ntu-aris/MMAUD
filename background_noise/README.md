# 🔊 MMAUD extracted background noise

**6,588 NumPy files · 12 original groups · 5.057 GB**

Background-noise arrays extracted for MMAUD and supplied by the dataset maintainer. The original `np_data_align` folder structure, filenames and file bytes are preserved.

**[Browse / download](https://huggingface.co/datasets/Yuan-Shenghai/MMAUD/tree/main/background_noise/np_data_align) · [Original Google Drive folder](https://drive.google.com/drive/folders/1b0CzLFp_F1DHpxiAB3TYNQZiaF3KLfTd) · [Source manifest](https://huggingface.co/datasets/Yuan-Shenghai/MMAUD/resolve/main/metadata/BACKGROUND_NOISE_SOURCE_MANIFEST.json) · [SHA-256 checksums](https://huggingface.co/datasets/Yuan-Shenghai/MMAUD/resolve/main/background_noise/SHA256SUMS.txt)**

## Array format

Each `.npy` file stores a two-dimensional **`float32`** array with **4 columns**. Nonempty arrays have **48,000 rows**, giving shape **`(48000, 4)`**. Load them with `numpy.load(..., allow_pickle=False)`.

The source contains **4 empty arrays** with shape `(0, 4)`: `10/0.npy`, `11/0.npy`, `12/0.npy`, `b9/0.npy`. These files are kept unchanged. Skip them when constructing batches.

Folder names are retained exactly, including `10`, `11` and `12`. Filenames are numeric source indices; the mirror does not rename or resample the arrays.

## Files by group

| Group | NPY files | Size (decimal MB) | Empty arrays |
|:---|---:|---:|---:|
| [b1](https://huggingface.co/datasets/Yuan-Shenghai/MMAUD/tree/main/background_noise/np_data_align/b1) | 1,183 | 908.695 | 0 |
| [b2](https://huggingface.co/datasets/Yuan-Shenghai/MMAUD/tree/main/background_noise/np_data_align/b2) | 898 | 689.779 | 0 |
| [b3](https://huggingface.co/datasets/Yuan-Shenghai/MMAUD/tree/main/background_noise/np_data_align/b3) | 1,063 | 816.520 | 0 |
| [b4](https://huggingface.co/datasets/Yuan-Shenghai/MMAUD/tree/main/background_noise/np_data_align/b4) | 1,621 | 1245.135 | 0 |
| [b5](https://huggingface.co/datasets/Yuan-Shenghai/MMAUD/tree/main/background_noise/np_data_align/b5) | 978 | 751.229 | 0 |
| [b6](https://huggingface.co/datasets/Yuan-Shenghai/MMAUD/tree/main/background_noise/np_data_align/b6) | 79 | 60.682 | 0 |
| [b7](https://huggingface.co/datasets/Yuan-Shenghai/MMAUD/tree/main/background_noise/np_data_align/b7) | 45 | 34.566 | 0 |
| [b8](https://huggingface.co/datasets/Yuan-Shenghai/MMAUD/tree/main/background_noise/np_data_align/b8) | 48 | 36.870 | 0 |
| [b9](https://huggingface.co/datasets/Yuan-Shenghai/MMAUD/tree/main/background_noise/np_data_align/b9) | 174 | 132.886 | 1 |
| [10](https://huggingface.co/datasets/Yuan-Shenghai/MMAUD/tree/main/background_noise/np_data_align/10) | 168 | 128.278 | 1 |
| [11](https://huggingface.co/datasets/Yuan-Shenghai/MMAUD/tree/main/background_noise/np_data_align/11) | 192 | 146.713 | 1 |
| [12](https://huggingface.co/datasets/Yuan-Shenghai/MMAUD/tree/main/background_noise/np_data_align/12) | 139 | 106.002 | 1 |
| **Total** | **6,588** | **5057.355** | **4** |

## Load one file

```python
from huggingface_hub import hf_hub_download
import numpy as np

path = hf_hub_download(
    repo_id="Yuan-Shenghai/MMAUD",
    repo_type="dataset",
    filename="background_noise/np_data_align/b1/5.npy",
)
array = np.load(path, allow_pickle=False)
print(array.shape, array.dtype)
```

## Download a group or the full collection

```python
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="Yuan-Shenghai/MMAUD",
    repo_type="dataset",
    local_dir="MMAUD",
    allow_patterns=["background_noise/np_data_align/b1/*"],
)
```

Use `allow_patterns=["background_noise/*"]` to download all 12 groups, this guide, the reading example and the checksum list. From the downloaded `MMAUD` directory, run `python background_noise/load_example.py background_noise/np_data_align/b1/5.npy` to inspect a local file.

## Provenance and verification

Published on **28 October 2026** from the maintainer-provided public Drive folder. Every original file was checked against Google's CRC32C response, parsed as NumPy data and assigned a SHA-256 digest. Every mirrored array was then downloaded anonymously from Hugging Face in full and matched by size and SHA-256. The source manifest records every Drive file ID and its repository path.

This addition is listed separately from the original V1/V2/V3 collection and its `supplementary/noise.bin` file. It does not replace any earlier recording.

## License and citation

Distributed with MMAUD under **[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)**. Cite the [MMAUD ICRA 2024 paper](https://doi.org/10.1109/ICRA57147.2024.10610957); the [dataset BibTeX](https://huggingface.co/datasets/Yuan-Shenghai/MMAUD/resolve/main/MMAUD_ICRA2024.bib) is available separately.
