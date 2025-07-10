def bubble_sort(arr):
    """
    冒泡排序算法
    时间复杂度: O(n²)
    空间复杂度: O(1)
    稳定性: 稳定
    """
    n = len(arr)
    
    # 外层循环控制排序轮数
    for i in range(n):
        # 设置标志位，如果一轮中没有交换，说明已经有序
        swapped = False
        
        # 内层循环进行相邻元素比较和交换
        # 每轮排序后，最大的元素会"冒泡"到末尾，所以内层循环可以减少i次
        for j in range(0, n - i - 1):
            # 如果前一个元素大于后一个元素，则交换它们
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # 如果这一轮没有发生交换，说明数组已经有序，可以提前退出
        if not swapped:
            break
    
    return arr


def bubble_sort_optimized(arr):
    """
    优化版冒泡排序
    记录最后一次交换的位置，下一轮只需要比较到该位置
    """
    n = len(arr)
    last_swap = n - 1  # 记录最后一次交换的位置
    
    while last_swap > 0:
        current_swap = 0  # 当前轮次最后一次交换的位置
        
        for j in range(last_swap):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                current_swap = j
        
        last_swap = current_swap
    
    return arr


# 测试代码
if __name__ == "__main__":
    # 测试用例
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 4, 6, 1, 3],
        [1],
        [],
        [3, 3, 3, 3],
        [9, 8, 7, 6, 5, 4, 3, 2, 1]
    ]
    
    print("=== 冒泡排序测试 ===")
    
    for i, test_arr in enumerate(test_cases, 1):
        print(f"\n测试用例 {i}:")
        print(f"原始数组: {test_arr}")
        
        # 创建副本进行排序
        arr_copy = test_arr.copy()
        sorted_arr = bubble_sort(arr_copy)
        print(f"排序结果: {sorted_arr}")
        
        # 验证排序结果
        is_sorted = sorted_arr == sorted(test_arr)
        print(f"排序正确: {is_sorted}")
    
    print("\n=== 优化版冒泡排序测试 ===")
    
    for i, test_arr in enumerate(test_cases, 1):
        print(f"\n测试用例 {i}:")
        print(f"原始数组: {test_arr}")
        
        # 创建副本进行排序
        arr_copy = test_arr.copy()
        sorted_arr = bubble_sort_optimized(arr_copy)
        print(f"排序结果: {sorted_arr}")
        
        # 验证排序结果
        is_sorted = sorted_arr == sorted(test_arr)
        print(f"排序正确: {is_sorted}")


# 性能测试函数
def performance_test():
    """性能测试：比较普通冒泡排序和优化版冒泡排序"""
    import time
    import random
    
    # 生成测试数据
    test_size = 1000
    test_data = [random.randint(1, 1000) for _ in range(test_size)]
    
    print(f"\n=== 性能测试 (数组大小: {test_size}) ===")
    
    # 测试普通冒泡排序
    arr1 = test_data.copy()
    start_time = time.time()
    bubble_sort(arr1)
    normal_time = time.time() - start_time
    print(f"普通冒泡排序耗时: {normal_time:.4f} 秒")
    
    # 测试优化版冒泡排序
    arr2 = test_data.copy()
    start_time = time.time()
    bubble_sort_optimized(arr2)
    optimized_time = time.time() - start_time
    print(f"优化版冒泡排序耗时: {optimized_time:.4f} 秒")
    
    # 验证结果一致性
    is_consistent = arr1 == arr2
    print(f"结果一致性: {is_consistent}")


# 运行性能测试这是测试代码
if __name__ == "__main__":
    performance_test()
    #将performance_test()函数结果写入到txt文件中
    import io
    import sys

    # 捕获performance_test()的输出并写入文件
    with open('performance_test.txt', 'w', encoding='utf-8') as f:
        old_stdout = sys.stdout
        sys.stdout = f
        try:
            performance_test()
        finally:
            sys.stdout = old_stdout
