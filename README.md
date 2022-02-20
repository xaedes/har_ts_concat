# har_ts_concat
Extract and concat .ts files from HTTP Archive format files (.har)

With Browser Devtools one can save .har file containing whole communication of a website.
In Chrome: Open "Network" tab in DevTools, press Ctrl+R to record the transmitted data, wait for end of transmission, right click any file and choose "Save all as HAR with content".
To extract and concat all transmitted .ts files you can use this tool.

```shell
python har_ts_concat.py filename.har
```

This will create "filename.har.ts".
