import datetime


def count_errors_with_code_in_time_range(log_file, code, time_begin, time_end):
    time_begin_dt = datetime.datetime.fromisoformat(time_begin)
    time_end_dt = datetime.datetime.fromisoformat(time_end)
    error_count = 0
    with open(log_file, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) == 3 and parts[1] == str(code):
                print(parts)
                timestamp = int(parts[0])
                log_time = datetime.datetime.fromtimestamp(timestamp)
                if time_begin_dt <= log_time <= time_end_dt:
                    error_count += 1

    return error_count


if __name__ == '__main__':
    log_file = 'output.log'
    code = 200
    time_begin = '2024-03-21T05:38:18'
    time_end = '2024-04-15T23:59:59'
    errors_count = count_errors_with_code_in_time_range(log_file, code, time_begin, time_end)
    print(f"Количество ошибок с кодом {code} за период с {time_begin} по {time_end}: {errors_count}")
