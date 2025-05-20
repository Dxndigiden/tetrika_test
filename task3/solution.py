class TimeIntervalAnalyzer:
    def __init__(self, lesson: list[int], pupil: list[int], tutor: list[int]):
        '''Инициализация интервалов урока, ученика и учителя.'''
        if len(lesson) != 2 or lesson[0] >= lesson[1]:
            raise ValueError('Неверный интервал урока')
        if len(pupil) % 2 or len(tutor) % 2:
            raise ValueError('Непарное число значений в интервалах')
        self.lesson = (lesson[0], lesson[1])
        self.pupil = self._to_pairs(pupil)
        self.tutor = self._to_pairs(tutor)

    def _to_pairs(self, times: list[int]) -> list[tuple[int, int]]:
        '''Преобразует список времен в пары интервалов.'''
        return [(times[i], times[i + 1]) for i in range(0, len(times), 2)]

    def _intersect_intervals(self, a: list[tuple[int, int]],
                             b: list[tuple[int, int]]) -> list[tuple[int, int]]:
        '''Возвращает пересечения двух списков интервалов.'''
        result = []
        i = j = 0
        while i < len(a) and j < len(b):
            start = max(a[i][0], b[j][0])
            end = min(a[i][1], b[j][1])
            if start < end:
                result.append((start, end))
            if a[i][1] < b[j][1]:
                i += 1
            else:
                j += 1
        return result

    def _merge_intervals(self, intervals: list[tuple[int, int]]
                         ) -> list[tuple[int, int]]:
        '''Объединяет пересекающиеся интервалы в один.'''
        if not intervals:
            return []
        intervals.sort()
        merged = [intervals[0]]
        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                merged[-1] = (last[0], max(last[1], current[1]))
            else:
                merged.append(current)
        return merged

    def calculate(self) -> int:
        '''Вычисляет суммарное время пересечения ученик+учитель на уроке.'''
        lesson_interval = [self.lesson]
        pupil_on_lesson = self._intersect_intervals(self.pupil, lesson_interval)
        tutor_on_lesson = self._intersect_intervals(self.tutor, lesson_interval)
        pupil_merged = self._merge_intervals(pupil_on_lesson)
        tutor_merged = self._merge_intervals(tutor_on_lesson)
        common = self._intersect_intervals(pupil_merged, tutor_merged)
        return sum(end - start for start, end in common)


def appearance(intervals: dict[str, list[int]]) -> int:
    '''Подсчитывает общее время пересечения по словарю интервалов.'''
    if not all(k in intervals for k in ('lesson', 'pupil', 'tutor')):
        raise ValueError('Входные данные неполные')
    analyzer = TimeIntervalAnalyzer(
        lesson=intervals['lesson'],
        pupil=intervals['pupil'],
        tutor=intervals['tutor']
    )
    return analyzer.calculate()
