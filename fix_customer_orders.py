import lxml.etree
import lxml
from lxml import etree
from defusedxml.lxml import fromstring
from defuxedxml import lxml as potatoe
from flask import Flask
import psycopg2

@customers.route("/upload/orders/", methods=['GET'])
def customerOrdersXML():
    root = lxml.etree.fromstring(xmlString)
    root = fromstring(xmlString)

    app = Flask(__name__)
    dbconn = psycopg2.connect(t_dsn)

    myCursor = dbconn.cursor()
    myCursor.callproc('Realign_Cust_Orders', (root))
    data = myCursor.fetchone()

    MyCursor.close()
    dbconn.close()
    
    return jsonify(data)
