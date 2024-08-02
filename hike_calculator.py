class sal:
    def est_sal(self,cur_sal,years,avg_hike):
        self.cur_sal = cur_sal
        self.years = years
        self.avg_hike = avg_hike
        import datetime as dt
        now = dt.datetime.now().strftime("%Y")
        for y in range(years):
            increment_sal = (cur_sal/100) * avg_hike
            total_sal = round(float(cur_sal) + float(increment_sal))
            cur_sal = total_sal
            now = int(now) + 1
            print("In the year",now,"Expected Salary is:", "{:,}".format(total_sal))

sal = sal()
sal.est_sal(2550000,6,12)