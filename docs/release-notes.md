# Changelog

所有对该项目的重要更改都将记录在此文件中。

---
## [[0.1.9](https://github.com///compare/v0.1.8..v0.1.9)] - 2024-10-26

### Bug 修复

- MVApi 注释错误 - ([0ace5cf](https://github.com///commit/0ace5cf2c6f5b7b03c5f63f396d45be64edfb35b)) 
- 修复获取逐字歌词未解析问题  - ([26929f2](https://github.com///commit/26929f26e4f61c5d5f68161cbe360f437ff50820)) 

### 功能更新

- 支持获取专辑封面链接  - ([7fe9644](https://github.com///commit/7fe964427f6c126a70173554bcdc5284e54331b2)) 

### 功能重构

- **(LoginApi)** [**breaking**] 重构 LoginApi  - ([9244c0e](https://github.com///commit/9244c0ebe8981ca2a00afb1fe367175b1b1a39c0)) 

### 文档更新

- 自动生成 Release Notes - ([5b3dfa6](https://github.com///commit/5b3dfa6e9ec89ad00c0d88f71b4ac16f8732ef39)) 
- 更新 Readme - ([485d988](https://github.com///commit/485d988c991b833d0f79ae7f86e5d1057fdff0dc)) 
- Update exceptions.md - ([a86f4a1](https://github.com///commit/a86f4a1d918fae7df8bccb25faab5b0751e91ae4)) 

### 构建配置

- 更新依赖版本 - ([1a42f97](https://github.com///commit/1a42f9707939ec86f0d0544ef771875018589782)) 

## [[0.1.8](https://github.com///compare/v0.1.7..v0.1.8)] - 2024-10-05

### 功能更新

- `get_song_urls` 更好的 Typing Hints  - ([02a62f5](https://github.com///commit/02a62f57d083b2b5d7c98ad5078ede521c99045d)) 
- 支持 UserApi  - ([7a99429](https://github.com///commit/7a994290cb298a868963d325dccab4a908e5fd9a)) 
- 支持检测凭证是否过期  - ([3a2b011](https://github.com///commit/3a2b011445479327dd433bc934685ac0088b1ef7)) 
- 支持在事件循环已经运行时同步执行异步代码  - ([b8190f5](https://github.com///commit/b8190f5663ca6c61ff622f18d0c14d065fe5c38d)) 
- 支持 ogg 640kbps 获取  - ([fe1660e](https://github.com///commit/fe1660ed86da7e1bb1bbc05b163af4acfd54205e)) 

### 功能重构

- 重构 ApiException  - ([11298e9](https://github.com///commit/11298e9c3f225b280ad654ab0b63d4c7455dc895)) 

## [[0.1.7](https://github.com///compare/v0.1.6..v0.1.7)] - 2024-09-15

### 功能更新

- 支持 LyricApi  - ([a5534b5](https://github.com///commit/a5534b5975bd95e45a5022eafd994362d1046f16)) 
- 支持获取 OGG 320kbps  - ([7d66486](https://github.com///commit/7d66486379e8009a60514806d1373f51840010be)) 
- 支持获取加密和试听文件  - ([bb6cf81](https://github.com///commit/bb6cf816a4bb79c5b846e211f4a216b5764dc4de)) 

### 文档更新

- 简化贡献文档  - ([3bae431](https://github.com///commit/3bae4311368f557d3f83e1b34a9efbe84c43b046)) 

## [[0.1.6](https://github.com///compare/v0.1.5..v0.1.6)] - 2024-08-25

### Bug 修复

- 注释错误 - ([0afd820](https://github.com///commit/0afd820776e117a0d15c282ec8c258c49d0a48e3)) 

### 功能更新

- 迁移到 httpx  - ([99fb2d9](https://github.com///commit/99fb2d9e4a1468da49f155beb4d08d43e99abccb)) 

### 功能重构

- 重构 Api 代码  - ([9e63a1e](https://github.com///commit/9e63a1eb4a8cc01a235545c669881b92bafe5868)) 

### 文档更新

- 优化贡献文档 - ([68c23c3](https://github.com///commit/68c23c32dd98596f67bdc91aeea12892680aa49c)) 
- 更新贡献指南 - ([d04053b](https://github.com///commit/d04053b13d1776054429f5477a6be3aadeef1d16)) 

## [[0.1.5](https://github.com///compare/v0.1.4..v0.1.5)] - 2024-08-03

### Bug 修复

- 未使用上下文管理器时报错 - ([bc647fa](https://github.com///commit/bc647fa9a033bf6f661fb633611293f8c84e40c9)) 
- 修复一些小错误 - ([1fc449a](https://github.com///commit/1fc449a8c228a8dcc166efd35b84670550c6c2e4)) 
- v0.1.4 未包含库文件 - ([7963f54](https://github.com///commit/7963f547fbfa5bcdcd90c4776d9f1776211f41fa)) 

### 功能更新

- 增加对 albumId 的支持 - ([d81de7f](https://github.com///commit/d81de7f532940ef3e802d36e3341d1b98d1bc63d)) 

### 文档更新

- 更新 readme - ([a454e21](https://github.com///commit/a454e21183277e0ebf7420cbee76bd549c73c7f0)) 

## [[0.1.4](https://github.com///compare/v0.1.3..v0.1.4)] - 2024-07-28

### 构建配置

- 更新 pyproject.toml - ([aad543b](https://github.com///commit/aad543b58fe73f46d0eaf6f552dd9a82ad7ca0c5)) 

## [[0.1.3](https://github.com///compare/v0.1.2..v0.1.3)] - 2024-07-27

### 文档更新

- 更完善的 API 文档  - ([2f62297](https://github.com///commit/2f62297e19de86e5c6ee7f88f0a58efe74cd2d47)) 

### 构建配置

- 迁移依赖管理工具为 PDM  - ([9262b5c](https://github.com///commit/9262b5c65ec757329fd729308da28bf47e059951)) 

## [[0.1.2](https://github.com///compare/v0.1.1..v0.1.2)] - 2024-07-21

### Bug 修复

- 部分类型错误 - ([f188f6e](https://github.com///commit/f188f6ef7e034cc3dfef73dd6ab84ad684393fd3)) 
- Fatal error on SSL transport - ([81a00c7](https://github.com///commit/81a00c74893b23946d46bcb5854b46f15c3ebd8f)) 
- python3.9 union syntax - ([4475513](https://github.com///commit/4475513e9849619bb347d3aa776d45cd831707ac)) 
- `Api`传入`Credential`无效 - ([eb1fe62](https://github.com///commit/eb1fe620afa25d68590002c5311eb368a92ca255)) 

### 功能更新

- **(login)** 添加报错信息，优化二维码获取 - ([721546f](https://github.com///commit/721546f45022edd819fab11c773962cf1db9c0a8)) 
- 更好的错误输出 - ([05ea8fe](https://github.com///commit/05ea8fec7e780195b89d6354af3bb714d1ebb07a)) 
- 懒获取QIMEI36 - ([218a740](https://github.com///commit/218a740136cef98082e840c75a3c4393c2caa0be)) 

### 功能重构

- 重构 `LoginApi` 代码 - ([a44d5ab](https://github.com///commit/a44d5ab35c846aa9483bfa76e94838e78fba4fbb)) 
- 重构代码  - ([9b17bf6](https://github.com///commit/9b17bf626094376dbfa314c5ac095db396a1e5a7)) 

### 性能优化

- 优化 LoginApi - ([bcdae55](https://github.com///commit/bcdae55e61fb7ee52db03643f235fc6a165e0e27)) 
- 优化 TopApi - ([46a1965](https://github.com///commit/46a196566641d199d12fd2540d0d8575fc9ebf41)) 

### 构建配置

- 移除不必要的开发依赖 - ([3d1dd29](https://github.com///commit/3d1dd292e87dd17c5be4e95d5d50ca23b60e40b7)) 

## [[0.1.1](https://github.com///compare/v0.1.0..v0.1.1)] - 2024-07-14

### Bug 修复

- 修改错误注释  - ([1a36d71](https://github.com///commit/1a36d7138c9f21fe13d08e4731922cc68e454cdc)) 
- import issue - ([cd72cd7](https://github.com///commit/cd72cd7809d371b2b17117c4c78d8eb31a3327cb)) 

### 功能更新

- **(SingerApi)** 添加 SingerApi Api - ([506faaa](https://github.com///commit/506faaa60f7ec1336dc2532dc4dc2006ed167990)) 
- **(SongApi)** 歌曲Api支持传入Credential - ([07e7a09](https://github.com///commit/07e7a0994ac320d0892f94a6da386684d5c5c7a7)) 
- **(SongApi)** 增加获取 Album, Singer - ([606a163](https://github.com///commit/606a1632a6521c34e50c6631f0a0b6de9d292eb8)) 
- Singer API  - ([b137846](https://github.com///commit/b137846ed87d43e15e9078b90203b4e03126d423)) 
- 支持 `__repr__` 和 `__str__` - ([7959f85](https://github.com///commit/7959f85b388e8b3150b2123a229ffa8b6aff6730)) 
- 增加获取歌手列表 API - ([ae00447](https://github.com///commit/ae00447e00aec2615781f06a6b421e2e4db77aba)) 
- add Singer API data - ([dd641e5](https://github.com///commit/dd641e5b010cb309875903d6ebe7c3aed8d82926)) 

### 性能优化

- 优化获取多个歌曲播放链接性能 - ([2168c07](https://github.com///commit/2168c0795b3f1d2a6ac9b83fbfb11239bdb0241b)) 

### 文档更新

- update readme - ([203c264](https://github.com///commit/203c2648b5510d103a58d6a9857b4d392aa2f97f)) 
- 添加 API 文档 - ([b2d2a8e](https://github.com///commit/b2d2a8eecd2a763ca27d94aa222526b7d08c2a8b)) 
- 更新 TODO - ([5b72d8d](https://github.com///commit/5b72d8da90401644e0224b9c1d9a6dd08eec0c57)) 

## [0.1.0] - 2024-06-07

### 功能更新

- add Top API - ([6785b4b](https://github.com///commit/6785b4b2bc0a729f3291c7b50d6fa35726b6dac2)) 
- add MV API - ([016f40b](https://github.com///commit/016f40b5b3c3f355128275045332cfb9ec0cc864)) 
- add Album API - ([e827510](https://github.com///commit/e827510dc8e3ce2931a90006243dd735adbefefd)) 
- add Songlist API - ([5c9b045](https://github.com///commit/5c9b04558ea3f32037cec62a019f0c4081796b9d)) 
- add Login API - ([480656e](https://github.com///commit/480656e06911267c2ce6f61c5a7f8bb647813e78)) 
- add Song API - ([6be6382](https://github.com///commit/6be638203adc2bc86b6e4b525a4011997174b4f3)) 
- add Search API - ([7e71614](https://github.com///commit/7e71614367995c8e69fa51bdb396f9ae9937ac1f)) 

### 功能重构

- some functions directly return Class Song - ([40e2c11](https://github.com///commit/40e2c11d6f18a73276e2bb675b6a9baabc2f0999)) 

### 构建配置

- update pyproject.toml - ([6320fdb](https://github.com///commit/6320fdbf491f926eb9ce673c5349b8638d64ee75)) 

<!-- generated by git-cliff -->
