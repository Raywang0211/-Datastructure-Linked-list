## 簡介：

鏈結串列也是一種儲存資料的方法由節點所組成的有序串列，與一般陣列最大不同在於鏈結串列可以將資料存放在不連續的記憶體中而一般陣列必須存在一個連續的記憶體當中。

鏈結串列又可以分成

1. 單向 Single linked list
2. 雙向  Double linked list
3. 環狀 Circular linked list

## 特性:

- 可以儲存在非連續的記憶體中
- 儲存的資料型態可以不固定
- 一個節點包含資料與指標
- 插入或是刪除節點很方便
- 只能進行循序的訪問(不能透過index訪問)

## 構造:

由多個node組成，每一個node包含了資料與指標

1. 資料: 當下這個node存放的資料內容
2. 指標: 下一個node存放的位置，若為雙向則會包含兩個指標，除了下一個node位置之外也會放上一個node的位置。

若不是環狀鏈結則整個鏈結最末端都會址到NULL代表結束。

## 儲存方式:

Single linked list
reference image 
Double linked list
reference image 

Circular linked list