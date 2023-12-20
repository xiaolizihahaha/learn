package test

import (
	"fmt"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
)

func Test1() {
	var str1, str2 string = "hello", "world"
	var num int = 123

	total := fmt.Sprintf("hi,%d!%s,%s", num, str1, str2)
	fmt.Println(total)

	mux := gin.Default()
	mux.GET("/time", func(c *gin.Context) {
		m := map[string]string{
			"time": time.Now().Format("2006-07-01"),
		}
		c.JSON(http.StatusOK, m)
	})

	err := mux.Run("0.0.0.0:3000")
	fmt.Println(err)
}
