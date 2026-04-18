from copy import deepcopy


class Report:
    def __init__(self, title, sections):
        self.title = title
        self.sections = sections

    def clone(self):
        return deepcopy(self)


if __name__ == "__main__":
    report = Report("Monthly", ["summary", "charts"])
    copy_report = report.clone()
    copy_report.title = "Monthly Copy"
    copy_report.sections.append("appendix")

    print(report.title, report.sections)
    print(copy_report.title, copy_report.sections)

