# ThinkBoard
Python Flask Mysql Project

1. Clone this project.
2. Navigate to the project directory.
3. Set your envirnment variable.
4. Excute this command "pip install -e ." on command line.
5. Your are all set to go.

Note: Database should be there

Test Request: curl -X Post http://127.0.0.1:5000/api/product/getProductDetails -H "Content-type: application/json"  -d '{"Request":{"Header":{"DeviceId":"123","RequestTime":"1.34545","Version":"1.0","Product":"2"},"Body":{"StoreId":"12345","SPBarcodeId":"12374859493"}}}'



