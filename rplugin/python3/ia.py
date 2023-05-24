

#code =  """ 
#(defn scan* [opts]
#  (let [code-structures (diplomat.code-reader/code-structure-from-clj-files-in-directory! opts)
#        rules (rules.loader/init! opts)
#        scans-results (->> code-structures
#                           (pmap #(check-rules-in-code-structure % rules))
#                           (reduce concat))
#        scan-result-output (output/output scans-results opts)]
#    scan-result-output))
#"""
#
#print(CHAIN.run(code))
