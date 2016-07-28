## Scripts

```python
python convert-pktb.py [input-directory]
```

* `input-directory` is the directory containing the [Penn Korean Treebank](https://catalog.ldc.upenn.edu/LDC2006T09) files (e.g., `newswire`).
* It reads `*.fid` files and creates `*.parse` files consisting of the constituency trees in the current English Treebank format, and `*.raw` files consisting of the original text.
* The output is encoded in `UTF-8` instead of `EUC-KR`.
