# HTML 翻译项目

## 项目简介

本项目利用百度翻译 API 和 Python 实现 HTML 网页的翻译，能够保留原始样式。通过对 HTML 文件内容的预处理，去除多余的空白字符和换行，以确保翻译的准确性和完整性。

## 功能特点

- 读取和处理 HTML 文件，删除标签内的多余空白和换行。
- 调用百度翻译 API 进行文本翻译。
- 保存翻译后的 HTML 文件，保留原始样式。

## 环境要求

- Python 3.x
- `requests` 库
- `beautifulsoup4` 库
- `re` 库（Python 内置）

## 安装依赖

在项目目录下运行以下命令安装所需的库：

```bash
pip install requests beautifulsoup4
```

## 使用说明

1. 将需要翻译的 HTML 文件重命名为 `help.html`，并放置在项目根目录下。
2. 在代码中配置你的百度翻译 API 的 `APP_ID` 和 `SECRET_KEY`。
3. 运行 `翻译脚本.py` 文件，执行翻译操作。

```bash
python translate_script.py
```

4. 翻译完成后，结果将保存在 `translated_help_preview.html` 文件中。

## 代码说明

- **处理 HTML 文件**：通过正则表达式去除 HTML 标签内部的多余空白和换行。
- **调用翻译 API**：使用百度翻译 API 进行文本翻译，并将翻译结果替换原有文本。
- **保存翻译结果**：将翻译后的内容保存为新的 HTML 文件，确保格式一致。

## 注意事项

- 请确保在调用百度翻译 API 时遵循其使用条款和限制。
- 该项目中未包含对 API 限制的处理，可能会导致请求失败。

## 贡献

欢迎对本项目提出建议或进行贡献，请创建 Issue 或者提交 Pull Request。

## 许可证

本项目采用 MIT 许可证，具体内容请参见 [LICENSE](LICENSE) 文件。


