import json

from django.shortcuts import render
from CuoTeJe.models import ItemsInfo

# Create your views here.


def main_page(request):
    return render(request, "main.html")


def insert_data(request):
    ItemCategory = request.POST.get("Categories")
    Item_sub_No = request.POST.get("ItemNo")
    ItemNo = ItemCategory + Item_sub_No
    Answer = request.POST.getlist('checkbox_list')
    ItemDesc = request.POST.getlist('ItemDesc')

    # 加一点判断选项是不是空的
    if not Answer or not Item_sub_No:
        server_response = "答案为空！"
    else:
        if get_item(ItemNo) is not False:
            server_response = "已经记录了!"
        else:
            try:
                items_info = ItemsInfo(ItemNo=ItemNo, CorrectAnswer=Answer, ItemDesc=ItemDesc)
                items_info.save()
                server_response = "插入成功"
            except:
                server_response = "插入失败，数据库挂了！"
    return render(request, "insert.html", locals())


def query_data(request):
    ItemCategory = request.GET.get("Categories")
    Item_sub_No = request.GET.get("ItemNo")
    ItemNo = ItemCategory + Item_sub_No
    # 加一点判断选项是不是空的

    if not Item_sub_No:
        server_response = "请选择要查询的题目编号！"
    else:
        try:
            item_obj = ItemsInfo.objects.get(ItemNo=ItemNo)
            data = str_to_list(item_obj.CorrectAnswer)
            data_desc = item_obj.ItemDesc[2:][:-2]
        except:
            server_response = "没找到或者发生错误了!"
    return render(request, "query.html", locals())


def insert_data_page(request):
    return render(request, "insert.html")


def query_data_page(request):
    return render(request, "query.html")


def get_item(ItemNo):
    try:
        return ItemsInfo.objects.get(ItemNo=ItemNo)
    except ItemsInfo.DoesNotExist:
        return False


def str_to_list(string):
    answer = []
    str_len = len(string)
    for i in range(2, str_len, 5):
        answer.append(string[i])
    return json.dumps(answer)



