<div align="center">
  <img src="dist/assets/orbi-icon.png" width="112" alt="Orbi app icon">
  <h1>Orbi for Mac</h1>
  <p><strong>小小刘海，大有可为。<br>A little notch. A lot more possibility.</strong></p>
  <p>音乐、日程与剪贴板，触手可及。<br>Music, calendar, and clipboard — right at the top of your Mac.</p>
  <p>
    <a href="https://kaitangkevin.github.io/orbi-website/">官方网站 · Website</a> ·
    <a href="https://kaitangkevin.github.io/orbi-website/download/">下载与使用 · Download</a> ·
    <a href="#关于开发者--about-the-developer">独立开发者 · Developer</a> ·
    <a href="#english">English</a>
  </p>
  <p><strong>macOS · Orbi 1.0 · 独立开发 · 中英双语</strong></p>
</div>

---

## 关于 Orbi

Orbi 是一款面向 Mac 的轻量顶部工作台。它把音乐控制、今日日程和文字剪贴板整合在屏幕顶部的刘海区域：鼠标移入时展开，移开后收起，让你处理小事时少切换一个窗口。

这个项目关注的是日常使用中的细节：下一首歌、下一场安排、刚刚复制的一段文字。让它们更容易触达，同时把注意力留给正在做的事情。

> **仓库范围**：这里包含 Orbi 官网、产品展示素材和 DMG 安装包，不包含原生 macOS 应用源码。仓库公开可见不等于采用开源许可证；使用与转载边界见下方版权声明。

## 产品能力

| 功能 | 当前支持 | 使用边界 |
| --- | --- | --- |
| **刘海工作台** | 鼠标移入展开，移出后延迟收起；集中展示三个模块 | 主要界面在屏幕顶部，并提供菜单栏入口 |
| **Apple Music 控制** | 当前歌曲与艺人、播放 / 暂停、上一首 / 下一首 | 需要允许对“音乐”应用的自动化访问 |
| **音频状态** | 展示其他发声应用的名称、播放状态和音频律动 | 不代表对所有播放器都提供切歌和歌曲详情 |
| **今日日程** | 显示正在进行或接下来的日程、时间与所属日历 | 依赖 macOS 日历访问权限 |
| **文字剪贴板** | 最近 15 条文字记录、点选重新复制、清空历史 | 当前实现面向文字，不是文件或图片剪贴板 |
| **个性化设置** | 音乐 / 日历 / 剪贴板显示开关、开机启动 | 隐藏模块不等于撤销访问权限或停止后台监测 |
| **语言** | 中文、英文、跟随系统 | 官网也提供中英文切换 |

## 产品展示

以下三张截图来自**官网的产品交互演示**，使用示例内容，并非原生应用实拍。你可以在[官网](https://kaitangkevin.github.io/orbi-website/)体验展开、示例播放控制与模块切换。

<table>
  <tr>
    <th>产品首页</th>
    <th>文字剪贴板</th>
    <th>模块工作台</th>
  </tr>
  <tr>
    <td><img src="docs/screenshots/workspace.png" width="280" alt="Orbi 官网首页与收起的刘海演示"></td>
    <td><img src="docs/screenshots/clipboard.png" width="280" alt="Orbi 官网文字剪贴板功能展示"></td>
    <td><img src="docs/screenshots/modules.png" width="280" alt="Orbi 官网音乐、日历与剪贴板模块展示"></td>
  </tr>
</table>

### 安装图解

![Orbi 安装图解：打开 DMG、拖入 Applications、启动 Orbi](dist/assets/orbi-install-guide.png)

*由开发者提供的安装示意图。图中的 `Orbi.dmg` 对应本仓库的 `Orbi-1.0.dmg`。*

## 下载与首次使用

**[下载 Orbi 1.0（DMG）](https://kaitangkevin.github.io/orbi-website/downloads/Orbi-1.0.dmg)** · 约 3.4 MB · [完整安装与权限指南](https://kaitangkevin.github.io/orbi-website/download/)

1. 下载并打开 `Orbi-1.0.dmg`。
2. 将 Orbi 拖入 **Applications（应用程序）** 文件夹，等待复制完成。
3. 从“应用程序”中打开 Orbi；鼠标移至屏幕顶部中央，展开工作台。
4. 按功能用途查看系统权限请求，并在 Orbi 设置中调整模块和语言。

当前版本**没有 Apple Developer ID 签名证书**。macOS 可能无法验证开发者或检查应用安全性。只有确认来源可信、文件未被篡改并接受风险后，才按[安装指南](https://kaitangkevin.github.io/orbi-website/download/#install)及 [Apple 官方说明](https://support.apple.com/zh-cn/102445)处理首次打开提示。请勿关闭系统整体安全保护。

最低 macOS 版本和芯片兼容范围尚未正式确认，请勿据此假定支持所有 Mac。

### 权限与数据访问

- **日历**：用于读取并展示日程；当前应用请求日历完整访问权限。
- **自动化 · 音乐**：用于读取 Apple Music 信息并发送播放控制指令。
- **系统音频**：用于检测音频活动并显示律动，授权行为以系统提示为准。
- **剪贴板**：应用运行时监测新复制的文字。隐藏剪贴板模块不会停止监测；需要停止时请退出 Orbi。

官网交互演示使用示例数据，不会读取访客的音乐、日历或剪贴板。安装后的原生应用与官网演示是两个不同的运行环境。

## 关于开发者 / About the developer

我是 **[Kaitangkevin](https://github.com/Kaitangkevin)**，Orbi 的独立开发者。

Orbi 是我的个人产品项目。我希望从 Mac 上那些反复发生的小动作出发，做一款轻巧、清晰、容易融入日常的工具：需要时出现，专注时退到一旁。

我正在持续完善产品体验，也欢迎具体的使用反馈。对我来说，比不断增加功能更重要的是，让已有功能更自然、更可靠，让每一个交互都有明确的用途。

**Orbi 是独立开发项目，并非 Apple 官方产品，也不表示获得 Apple 的认可或背书。**

### 反馈与联系

欢迎通过 [GitHub Issues](https://github.com/Kaitangkevin/orbi-website/issues)提交功能建议、官网问题或使用反馈。请尽量附上 macOS 版本、Orbi 版本、复现步骤与预期行为；截图前请隐藏个人日程、剪贴板内容及其他隐私信息。

商业合作或内容使用授权，可先通过 [GitHub 个人主页](https://github.com/Kaitangkevin)联系开发者。请勿在公开 Issue 中提交密码、访问令牌或私人资料。

## 版权与使用声明

**Copyright © 2026 Kaitangkevin. All rights reserved. 保留所有权利。**

本项目未以 MIT、Apache、GPL 或其他开源许可证发布。除法律允许的使用、GitHub 平台条款所赋予的权利，以及另行取得的明确授权外：

- **禁止抄袭与冒名发布**：不得将本项目的代码、原创文案、图像或设计素材冒充为自己的原创成果，不得移除作者署名后重新发布。
- **禁止未经授权复制与改作**：不得复制、改编、转载或重新分发本项目中受版权保护的内容，也不得换名打包、制作衍生分发版本或用于商业销售。
- **禁止未经授权使用品牌素材**：不得使用 Orbi 名称、图标及视觉素材，使他人误认为你的产品、网站或服务由本开发者提供或授权。
- **公开可见不构成额外授权**：查看仓库或使用 GitHub 平台功能，不代表获得上述内容的商业使用、再分发或改作许可。引用来源本身也不等于取得授权。

欢迎分享本项目的**官方链接**。如需转载、使用素材、商业合作或其他授权，请先联系开发者并取得明确书面许可。

以上声明仅针对权利人依法享有权利的内容，不主张对通用功能、抽象创意或第三方资产的专有权。第三方组件、商标及素材的权利归其各自权利人，并适用各自的许可条款。

---

<a id="english"></a>

## English

### What is Orbi?

Orbi is an independently developed notch workspace for Mac. It brings music controls, today’s events, and recent copied text to the top of your screen. Hover to expand; move away to return to a compact view.

This repository contains the **website, presentation assets, and downloadable installer**, not the native macOS app’s source code. Public visibility does not make the project open source.

### Capabilities

- **Apple Music:** track and artist information, play/pause, and previous/next controls.
- **Audio activity:** app identity, playback state, and waveform for other audio sources; universal track control is not claimed.
- **Calendar:** today’s current or upcoming event, time, and calendar name.
- **Text clipboard:** up to 15 recent entries, select to copy again, and clear history.
- **Personalization:** module visibility, launch at login, and Chinese, English, or system language.

The screenshots above show the **website’s interactive recreations with sample content**, not native app captures. The installation illustration was supplied by the developer.

### Install

[Download Orbi 1.0](https://kaitangkevin.github.io/orbi-website/downloads/Orbi-1.0.dmg), open the DMG, drag Orbi into Applications, and launch it from there. Read the [setup and permissions guide](https://kaitangkevin.github.io/orbi-website/download/) before first use.

The current installer has no Apple Developer ID signing certificate. Review macOS warnings and only proceed if you trust the source and accept the risk. Minimum macOS and chip compatibility remain unconfirmed. Hiding a module does not revoke permissions; clipboard monitoring continues while the app runs.

### About the independent developer

I’m **[Kaitangkevin](https://github.com/Kaitangkevin)**, the independent developer behind Orbi. This is my personal product project, focused on making small, frequent interactions on the Mac easier to reach and less distracting. I’m continuing to refine the experience and welcome specific feedback through [Issues](https://github.com/Kaitangkevin/orbi-website/issues).

Orbi is independent and is not an official Apple product or endorsed by Apple.

### Copyright and permitted use

**Copyright © 2026 Kaitangkevin. All rights reserved.** No open-source license is granted.

Except where permitted by applicable law, GitHub’s platform terms, or express authorization, unauthorized copying, adaptation, redistribution, commercial exploitation, removal of attribution, and presenting protected project content as your own are prohibited. Do not use Orbi branding to imply affiliation or authorization. Attribution alone does not grant permission.

Sharing official project links is welcome. Contact the developer for written permission before reusing protected content. These notices cover only rights held by the relevant rights holder, not general functionality, abstract ideas, or third-party assets. Third-party rights and licenses remain with their respective owners.

---

<details>
<summary><strong>Repository guide / 仓库维护说明</strong></summary>

| Path | Purpose |
| --- | --- |
| `dist/product.js` | Product presentation and interactive demos |
| `dist/pages.js` | Download guide and about page |
| `dist/app.js` | Navigation and language preference |
| `dist/style.css` | Styling and responsive layouts |
| `dist/assets/` | Website images |
| `dist/downloads/` | Installer |
| `docs/screenshots/` | README screenshots |
| `.github/workflows/pages.yml` | GitHub Pages deployment |
| `scripts/build-pages.py` | Deployment base-path preparation |

Authorized maintenance: preview with `python3 -m http.server 4173 --directory dist`. Pushing to `main` deploys the website through GitHub Actions. The generated `_site/` directory is published; repository documentation is not included in that output.

</details>
