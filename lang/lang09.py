"""
断言示例

@author Aaric
@version 0.5.0-SNAPSHOT
"""

import sys

assert "win32" in sys.platform, "请在 Windows 平台运行，谢谢！"

print("platform: {}".format(sys.platform))
