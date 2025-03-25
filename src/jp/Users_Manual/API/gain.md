# Gain

`Gain`は各振動子の位相/振幅を管理する構造体の総称であり, `Gain`を送信することで各振動子の位相/振幅を設定することができる.
SDKにはデフォルトでいくつかの種類の音場を生成するための`Gain`が用意されている.

- [Null](./gain/null.md) ‐ 何も出力しない
- [Focus](./gain/focus.md) - 単一焦点
- [Bessel](./gain/bessel.md) - ベッセルビーム
- [Plane](./gain/plane.md) - 平面波
- [Uniform](./gain/uniform.md) - すべての振動子を同じ位相/振幅で駆動
- [Custom](./gain/custom.md) - ユーザーが自由に位相/振幅を指定できる
- [Group](./gain/grouped.md) - 振動子をグループ化して, 各グループ毎に異なる`Gain`を適用
- [Holo](./gain/holo.md) - 多焦点音場
- [Cache](./gain/cache.md) - `Gain`の計算結果をキャッシュする
