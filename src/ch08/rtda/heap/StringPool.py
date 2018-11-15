from ch08.rtda.heap.Object import Object

class StringPool:

    internedStrings = {}

    @staticmethod
    def JString(loader, goStr):
        internedStr = StringPool.internedStrings.get(goStr)
        if internedStr:
            return internedStr

        chars = StringPool.stringToUtf16(goStr)
        jChars = Object(loader.loadClass("[C"), chars)

        jStr = loader.loadClass("java/lang/String").newObject()
        jStr.setRefVar("value", "[C", jChars)

        StringPool.internedStrings[goStr] = jStr
        return jStr

    @staticmethod
    def stringToUtf16(s):
        return s.decode("utf-16")

    @staticmethod
    def goString(jStr):
        charArr = jStr.getRefVar("value", "[C")
        return StringPool.utf16ToString(charArr.chars)

    @staticmethod
    def utf16ToString(s):
        return str(s)


