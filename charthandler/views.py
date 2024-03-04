import base64
import io
import json
import os
import time
import numpy as np
import matplotlib.pyplot as plt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
# 设置Matplotlib字体为SimHei,解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
"""
  直方图参数说明：
    hist_title('直方图名')
    hist_xlabel('x轴坐标标签')
    hist_ylabel('y轴坐标标签')
    hist_low('样本最小值')
    hist_high('样本最大值')
    hist_size('样本总体大小')
    hist_bins('直方图箱子数量')
    hist_histtype('直方图类型')
    hist_linewidth('直方图边缘线宽度')
    hist_grid_status('是否开启网格线')
    hist_alpha('网格线透明参数')
    hist_grid_linestyle('网格线线体类型')
"""
@csrf_exempt
def hist_generation(request):
    if request.method == 'POST':
        try:
            # Assuming the data sent from the frontend is in JSON format
            data = json.loads(request.body.decode('utf-8'))

            # Accessing the values from the JSON data
            hist_title = data.get('hist_title')
            hist_xlabel = data.get('hist_xlabel')
            hist_ylabel = data.get('hist_ylabel')
            hist_low = data.get('hist_low')
            hist_high = data.get('hist_high')
            hist_size = data.get('hist_size')
            hist_status = data.get('hist_status') if data.get('hist_status')!= None else False
            hist_gridtype = data.get('hist_gridtype') if data.get('hist_gridtype') != None else '-'
            # processing logic
            # 数据生成
            # 均匀分布
            data = np.random.uniform(low=int(hist_low), high=int(hist_high), size=int(hist_size))
            # 直方图参数设置
            hist_params = {
                'bins': 30,
                'histtype': 'step',
                'linewidth': 2,
            }
            # 创建直方图
            n, bins, patches = plt.hist(data, **hist_params)
            # 添加颜色渐变
            bin_centers = 0.5 * (bins[:-1] + bins[1:])
            col = bin_centers - min(bin_centers)
            col /= max(col)
            for c, p in zip(col, patches):
                plt.setp(p, 'color', plt.cm.get_cmap('viridis')(c))
            # 添加直方图上的数值标签
            for count, x in zip(n, bin_centers):
                plt.text(x, count + 5, f'{int(count)}', ha='center', va='bottom', color='white')
            # 添加边缘标签
            plt.title(hist_title)
            plt.xlabel(hist_xlabel)
            plt.ylabel(hist_ylabel)
            # 添加网格
            if(hist_status==True):
               plt.grid(hist_status, linestyle=hist_gridtype, alpha=0.6)

            # Saving the image in memory
            img_data = io.BytesIO()
            plt.savefig(img_data, format='png')
            img_data.seek(0)
            img_base64 = base64.b64encode(img_data.getvalue()).decode()

            plt.close()
            # Returning a JSON response with the image URL
            response_data = {'success': True, 'message': 'Chart data received successfully', 'image_data': img_base64}
            return JsonResponse(response_data)
        except Exception as e:
            # Handling errors
            response_data = {'success': False, 'error_message': str(e)}
            return JsonResponse(response_data, status=400)
    else:
        # Handling other HTTP methods
        response_data = {'success': False, 'error_message': 'Invalid HTTP method'}
        return JsonResponse(response_data, status=405)

"""
  折线图参数说明：
     line_title('折线图标题')
     line_xlabel('折线图x轴标签')
     line_ylabel('折线图y轴标签')
     line_start('数据生成起始值')
     line_stop('数据生成终止值')
     line_num('数据生成数量')
     line_type('函数类型')  :: y值
     line_color('函数颜色')  
     line_style('折线图线条类型')
"""
@csrf_exempt
def line_generation(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Accessing the values from the form
            line_title = data.get('line_title')
            line_xlabel = data.get('line_xlabel')
            line_ylabel = data.get('line_ylabel')
            linecharts_data = data.get('linecharts_data', [])


            # Process the data as needed
            # Create a figure and axis
            fig, ax = plt.subplots(figsize=(8, 6))
            # For example, you can save it to the database or perform any other actions
            # 创建一些示例数据
                # Process the data and plot the lines
            for item in linecharts_data:
                line_label = item.get('line_label')
                line_start = float(item.get('line_start'))
                line_stop = float(item.get('line_stop'))
                line_num = int(item.get('line_num'))
                line_functiontype = item.get('line_functiontype')
                line_colors = item.get('line_colors')

                # Create x values
                x = np.linspace(line_start, line_stop, line_num)

                # Create the corresponding NumPy function using a factory pattern
                function_factory = {
                        'sin(x)': np.sin,
                        'cos(x)': np.cos,
                        'sin(2x)': lambda x: np.sin(2 * x),
                        'cos(2x)': lambda x: np.cos(2 * x),
                        'exp(x)': np.exp,
                        'log(x)': np.log,
                 }

                if line_functiontype in function_factory:
                    np_function = function_factory[line_functiontype]
                    # Use np_function to generate y values based on x
                    y = np_function(x)

                    # Plot the line
                    ax.plot(x, y, label=line_label, linestyle='-', color=line_colors, linewidth=2)
            # 添加标题和标签
            plt.title(line_title)
            plt.xlabel(line_xlabel)
            plt.ylabel(line_ylabel)
            # 添加网格
            plt.grid(True)
            # 添加图例
            plt.legend()
            # Saving the image in memory
            img_data = io.BytesIO()
            plt.savefig(img_data, format='png')
            img_data.seek(0)
            img_base64 = base64.b64encode(img_data.getvalue()).decode()

            plt.close()
            # Returning a JSON response with the image URL
            response_data = {'success': True, 'message': 'Chart data received successfully', 'image_data': img_base64}
            return JsonResponse(response_data)

        except json.JSONDecodeError as e:
            # Handle JSON decoding error
            return JsonResponse({'error': 'Invalid JSON format in the request body.'}, status=400)

    else:
        # Return a method not allowed response for non-POST requests
        return JsonResponse({'error': 'Method not allowed. Only POST requests are allowed.'}, status=405)


"""
  箱型图参数说明：
     box_title('箱型图标题')
     box_xlabel('箱型图x轴标签')
     box_ylabel('箱型图y轴标签')
     box_xticklabels('x轴数据标签值')  ::  数组类型,有多少组就有多少个
     data_loc('样本起始值')
     data_scale('样本刻度')
     data_size('样本量')
     box_color('函数颜色')  :: 数组类型,有多少组就有多少个
"""
@require_POST
@csrf_exempt
def box_generation(request):
    box_colors = []
    generated_data = []

    try:
        # Assuming the data is sent as JSON
        data = json.loads(request.body)

        # Accessing values from the form
        box_title = data.get('box_title')
        box_xlabel = data.get('box_xlabel')
        box_ylabel = data.get('box_ylabel')
        boxcharts_data = data.get('boxcharts_data', [])



        for entry in boxcharts_data:
            loc = int(entry.get('box_loc'))
            scale = int(entry.get('box_scale'))
            size = int(entry.get('box_size'))
            # Generate data based on the provided parameters
            generated_data.append(np.random.normal(loc, scale, size).tolist())
            box_colors.append(entry.get('box_colors'))
        # Process the data as needed
        # 创造箱线图
        fig, ax = plt.subplots()
        # 箱线图
        boxplot = ax.boxplot(generated_data)
        # 自定义箱型图样式
        for box, color in zip(boxplot['boxes'], box_colors):
            box.set_color(color)
        # 设置图表标题和标签
        ax.set_title(box_title)
        ax.set_xticklabels(list(map(lambda entry: entry['box_label'], boxcharts_data)))
        ax.set_xlabel(box_xlabel)
        ax.set_ylabel(box_ylabel)
        # Saving the image in memory
        img_data = io.BytesIO()
        plt.savefig(img_data, format='png')
        img_data.seek(0)
        img_base64 = base64.b64encode(img_data.getvalue()).decode()

        plt.close()
        # Returning a JSON response with the image URL
        response_data = {'success': True, 'message': 'Chart data received successfully', 'image_data': img_base64}
        return JsonResponse(response_data)

    except json.JSONDecodeError as e:
        response_data = {'status': 'error', 'message': 'Invalid JSON format'}
        return JsonResponse(response_data, status=400)

    except Exception as e:
        response_data = {'status': 'error', 'message': str(e)}
        return JsonResponse(response_data, status=500)



"""
  饼图参数说明：
     pie_title('饼图标题')
     pie_sizes('饼图各个扇区大小') :: 数组类型，有多少组就多少个
     pie_labels('饼图各个扇区的标签')  ::  数组类型,有多少组就有多少个
     pie_colors('饼图各个扇区颜色')  ::  数组类型,有多少组就有多少个
     pie_explodes('饼图各个扇区的偏移量') ::  数组类型,有多少组就有多少个
"""
@csrf_exempt
def pie_generation(request):
    # Define global lists to store the data
    pie_sizes_list = []
    pie_labels_list = []
    pie_colors_list = []
    pie_explodes_list = []
    if request.method == 'POST':
        try:
            # Get the JSON data from the POST request
            data = json.loads(request.body)
            # Access the values from the form
            pie_title = data.get('pie_title')
            piecharts_data = data.get('piecharts_data', [])
            for chart_data in piecharts_data:
                pie_sizes = chart_data.get('pie_sizes')
                pie_labels = chart_data.get('pie_labels')
                pie_colors = chart_data.get('pie_colors')
                pie_explodes = chart_data.get('pie_explodes')
                # Store the data in the global lists
                pie_sizes_list.append(pie_sizes)
                pie_labels_list.append(pie_labels)
                pie_colors_list.append(pie_colors)
                pie_explodes_list.append(pie_explodes/1000)
                # Process each set of data as needed
                # 绘制饼图
                plt.pie(pie_sizes_list, explode=pie_explodes_list, labels=pie_labels_list, colors=pie_colors_list, autopct='%1.1f%%', startangle=90)
                # 添加图表标题
                plt.title(pie_title)
                # 设置相等的纵横比，使饼图成为一个圆形
                plt.axis('equal')


            # Saving the image in memory
            img_data = io.BytesIO()
            plt.savefig(img_data, format='png')
            img_data.seek(0)
            img_base64 = base64.b64encode(img_data.getvalue()).decode()

            plt.close()
            # Returning a JSON response with the image URL
            response_data = {'success': True, 'message': 'Chart data received successfully','image_data': img_base64}
            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})





