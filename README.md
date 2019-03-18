# ThinkBoard
Python Flask Mysql Project

Clone this project.
Navigate to the project directory.
Set your envirnment variable.
Excute this command "pip install -e ." on command line.
Your are all set to go.

Note: Database should be there, you can write a email 'swain.jeeten@gmail.com' for DB

Test Request: curl -X Post http://127.0.0.1:5000/api/product/getProductDetails -H "Content-type: application/json"  -d '{"Request":{"Header":{"DeviceId":"123","RequestTime":"1.34545","Version":"1.0","Product":"2"},"Body":{"StoreId":"12345","SPBarcodeId":"12374859493"}}}'
